from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_commit_msg import MAX_SUBJECT_LENGTH, validate_subject  # noqa: E402


@pytest.mark.parametrize(
    "message",
    (
        "feature: add hotel room search by occupancy\n",
        "bugfix: skip firebase write when feedback is empty\n\nMore detail.\n",
        "docs: describe ruff format checks\n",
        "refactor: extract sentiment weighting helper\n",
    ),
)
def test_valid_commit_subjects(message: str) -> None:
    assert validate_subject(message) is None


@pytest.mark.parametrize(
    "message",
    (
        "Add hotel room search\n",
        "Feature: add packing\n",
        "feature:Add room search\n",
        "feature: Add room search\n",
        "chore: tweak delays\n",
        "feature: " + "a" * (MAX_SUBJECT_LENGTH - len("feature: ") + 1) + "\n",
    ),
)
def test_invalid_commit_subjects(message: str) -> None:
    assert validate_subject(message) is not None
