"""Reject dependency pins that the installed Rasa release does not allow.

Patch and minor bumps of rasa or rasa-sdk are reported as needing a local
train. Major bumps fail. Other packages fail when they sit outside the
Requires-Dist ranges of the pinned rasa and rasa-sdk releases.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from packaging.requirements import Requirement
from packaging.utils import canonicalize_name
from packaging.version import Version

RASA_NAME = canonicalize_name("rasa")
SDK_NAME = canonicalize_name("rasa-sdk")
_PIN = re.compile(r"^\s*([A-Za-z0-9][A-Za-z0-9_.-]*)\s*([><=~!]+)\s*([0-9][A-Za-z0-9.*+!]*)")
RequiresLookup = Callable[[str, str], list[str]]


@dataclass(frozen=True)
class Pin:
    name: str
    operator: str
    version: Version


@dataclass(frozen=True)
class CheckResult:
    errors: tuple[str, ...]
    needs_train: bool


def parse_pins(text: str) -> dict[str, Pin]:
    pins: dict[str, Pin] = {}
    for line in text.splitlines():
        stripped = line.split("#", 1)[0].strip()
        if not stripped or stripped.startswith("-"):
            continue
        match = _PIN.match(stripped)
        if match is None:
            continue
        name = canonicalize_name(match.group(1))
        pins[name] = Pin(name, match.group(2), Version(match.group(3)))
    return pins


def requirements_by_name(requires_dist: list[str]) -> dict[str, list[Requirement]]:
    grouped: dict[str, list[Requirement]] = {}
    for raw in requires_dist:
        requirement = Requirement(raw)
        grouped.setdefault(canonicalize_name(requirement.name), []).append(requirement)
    return grouped


def _version_allowed(version: Version, requirements: list[Requirement]) -> bool:
    return all(version in requirement.specifier for requirement in requirements)


def _release_gap(old: Version, new: Version) -> str | None:
    if old == new:
        return None
    if old.major != new.major:
        return "major"
    if old.minor != new.minor:
        return "minor"
    return "patch"


def evaluate(
    base_text: str,
    head_text: str,
    lookup: RequiresLookup,
) -> CheckResult:
    base = parse_pins(base_text)
    head = parse_pins(head_text)
    errors: list[str] = []

    for required in (RASA_NAME, SDK_NAME):
        if required not in head:
            errors.append(f"missing {required} pin in the updated requirements")
    if errors:
        return CheckResult(tuple(errors), False)

    rasa = head[RASA_NAME]
    sdk = head[SDK_NAME]
    changed = {name: pin for name, pin in head.items() if name not in base or base[name] != pin}

    for name in (RASA_NAME, SDK_NAME):
        if name not in changed or name not in base:
            continue
        gap = _release_gap(base[name].version, head[name].version)
        if gap == "major":
            errors.append(f"{name} {head[name].version} is a major bump from {base[name].version}")

    try:
        rasa_requires = requirements_by_name(lookup("rasa", str(rasa.version)))
        sdk_requires = requirements_by_name(lookup("rasa-sdk", str(sdk.version)))
    except Exception as exc:  # noqa: BLE001 — surface lookup failures as a check error
        errors.append(f"could not read Rasa requirements: {exc}")
        return CheckResult(tuple(errors), False)

    sdk_rules = rasa_requires.get(SDK_NAME)
    if not sdk_rules:
        errors.append(f"rasa {rasa.version} does not declare a rasa-sdk requirement")
    elif not _version_allowed(sdk.version, sdk_rules):
        rendered = ", ".join(str(rule.specifier) for rule in sdk_rules)
        errors.append(f"rasa-sdk {sdk.version} does not satisfy rasa {rasa.version} ({rendered})")

    for name, pin in sorted(changed.items()):
        if name in (RASA_NAME, SDK_NAME):
            continue
        groups = []
        if name in rasa_requires:
            groups.append(rasa_requires[name])
        if name in sdk_requires:
            groups.append(sdk_requires[name])
        if not groups:
            continue
        if any(not _version_allowed(pin.version, group) for group in groups):
            errors.append(
                f"{name} {pin.version} is outside the range pinned by rasa {rasa.version}"
            )

    needs_train = not errors and any(name in changed for name in (RASA_NAME, SDK_NAME))
    return CheckResult(tuple(errors), needs_train)


def fetch_requires_dist(distribution: str, version: str) -> list[str]:
    url = f"https://pypi.org/pypi/{distribution}/{version}/json"
    with urllib.request.urlopen(url, timeout=30) as response:
        payload = json.load(response)
    return list(payload["info"].get("requires_dist") or [])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, required=True, help="base branch requirements.txt")
    parser.add_argument("--head", type=Path, required=True, help="pull request requirements.txt")
    parser.add_argument(
        "--github-output",
        type=Path,
        help="file that receives needs_train=true or needs_train=false",
    )
    args = parser.parse_args(argv)
    result = evaluate(
        args.base.read_text(encoding="utf-8"),
        args.head.read_text(encoding="utf-8"),
        fetch_requires_dist,
    )
    if args.github_output is not None:
        flag = "true" if result.needs_train else "false"
        with args.github_output.open("a", encoding="utf-8") as handle:
            handle.write(f"needs_train={flag}\n")
    if result.needs_train:
        print("rasa or rasa-sdk changed by a patch or minor release.")
        print("Merge waits on a local rasa train and rasa test against tests/test_stories.yml.")
        print("Do not add story tests unless that run fails.")
    if result.errors:
        for error in result.errors:
            print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
