from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_rasa_dep_range import evaluate  # noqa: E402

BASE = """
rasa~=2.8.34
rasa-sdk~=2.8.11
urllib3==1.26.18
firebase-admin==5.4.0
"""

RASA_2_8_34 = [
    "rasa-sdk (==2.8.11)",
    "numpy (>=1.19.2,<1.20.0)",
]
RASA_2_8_35 = [
    "rasa-sdk (==2.8.35)",
    "numpy (>=1.19.2,<1.20.0)",
]
RASA_2_9_0 = [
    "rasa-sdk (==2.9.0)",
    "numpy (>=1.19.2,<1.20.0)",
]
SDK_2_8_11 = ["urllib3 (>=1.26.5,<2.0.0)"]
SDK_2_8_35 = ["urllib3 (>=1.26.5,<2.0.0)"]
SDK_2_9_0 = ["urllib3 (>=1.26.5,<2.0.0)"]

REQUIRES = {
    ("rasa", "2.8.34"): RASA_2_8_34,
    ("rasa", "2.8.35"): RASA_2_8_35,
    ("rasa", "2.9.0"): RASA_2_9_0,
    ("rasa", "3.0.0"): ["rasa-sdk (==3.0.0)"],
    ("rasa-sdk", "2.8.11"): SDK_2_8_11,
    ("rasa-sdk", "2.8.12"): SDK_2_8_11,
    ("rasa-sdk", "2.8.35"): SDK_2_8_35,
    ("rasa-sdk", "2.9.0"): SDK_2_9_0,
    ("rasa-sdk", "3.0.0"): ["urllib3 (>=2,<3)"],
}


def lookup(distribution: str, version: str) -> list[str]:
    return REQUIRES[(distribution, version)]


def test_major_rasa_bump_fails() -> None:
    head = BASE.replace("rasa~=2.8.34", "rasa~=3.0.0")
    head = head.replace("rasa-sdk~=2.8.11", "rasa-sdk~=3.0.0")
    result = evaluate(BASE, head, lookup)
    assert result.needs_train is False
    assert any("major bump" in error for error in result.errors)


def test_patch_rasa_pair_needs_train() -> None:
    head = BASE.replace("rasa~=2.8.34", "rasa~=2.8.35")
    head = head.replace("rasa-sdk~=2.8.11", "rasa-sdk~=2.8.35")
    result = evaluate(BASE, head, lookup)
    assert result.errors == ()
    assert result.needs_train is True


def test_minor_rasa_pair_needs_train() -> None:
    head = BASE.replace("rasa~=2.8.34", "rasa~=2.9.0")
    head = head.replace("rasa-sdk~=2.8.11", "rasa-sdk~=2.9.0")
    result = evaluate(BASE, head, lookup)
    assert result.errors == ()
    assert result.needs_train is True


def test_sdk_patch_outside_rasa_pin_fails() -> None:
    head = BASE.replace("rasa-sdk~=2.8.11", "rasa-sdk~=2.8.12")
    result = evaluate(BASE, head, lookup)
    assert result.needs_train is False
    assert any("does not satisfy" in error for error in result.errors)


def test_urllib3_inside_sdk_range_passes() -> None:
    head = BASE.replace("urllib3==1.26.18", "urllib3==1.26.19")
    result = evaluate(BASE, head, lookup)
    assert result.errors == ()
    assert result.needs_train is False


def test_urllib3_2_fails() -> None:
    head = BASE.replace("urllib3==1.26.18", "urllib3==2.0.0")
    result = evaluate(BASE, head, lookup)
    assert result.needs_train is False
    assert any("urllib3 2.0.0 is outside" in error for error in result.errors)


def test_app_only_package_is_not_gated() -> None:
    head = BASE.replace("firebase-admin==5.4.0", "firebase-admin==6.2.0")
    result = evaluate(BASE, head, lookup)
    assert result.errors == ()
    assert result.needs_train is False


def test_unchanged_file_does_not_need_train() -> None:
    result = evaluate(BASE, BASE, lookup)
    assert result.errors == ()
    assert result.needs_train is False
