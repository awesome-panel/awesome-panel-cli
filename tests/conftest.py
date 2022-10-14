"""Shared fixtures for testing"""

from pathlib import Path

import pytest


@pytest.fixture()
def tmp_project_dir(tmpdir):
    """A temporary project directory"""
    Path(tmpdir / "pyproject.toml").write_text("something", encoding="utf8")
    return tmpdir
