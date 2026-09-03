"""Validate the first line of a Git commit message."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ALLOWED_PREFIXES = ("feature", "bugfix", "docs", "refactor")
MAX_SUBJECT_LENGTH = 100
_SUBJECT = re.compile(rf"^({'|'.join(ALLOWED_PREFIXES)}): [a-z].*")


def validate_subject(message: str) -> str | None:
    first_line = message.splitlines()[0] if message.strip() else ""
    if len(first_line) > MAX_SUBJECT_LENGTH:
        return f"first line must be at most {MAX_SUBJECT_LENGTH} characters"
    if not _SUBJECT.fullmatch(first_line):
        prefixes = "|".join(ALLOWED_PREFIXES)
        return (
            f"first line must match '{prefixes}: ' followed by a lowercase summary "
            f"(example: feature: add hotel room search by occupancy)"
        )
    return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="path to COMMIT_EDITMSG")
    args = parser.parse_args(argv)
    error = validate_subject(args.path.read_text(encoding="utf-8"))
    if error is None:
        return 0
    print(f"error: {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
