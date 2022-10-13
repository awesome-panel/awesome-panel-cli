"""We have shared functionality"""
from pathlib import Path

import pytest

from awesome_panel_cli import shared


def test_can_run_in_subprocess(mocker):
    """Can run command in subprocess"""
    # Givens
    spy = mocker.patch("subprocess.run")
    command = "echo hello"
    # When
    shared.run(command=command)
    # Then
    spy.assert_called_once_with("echo hello", check=True)


def test_get_project_root(tmpdir):
    """Can get project root"""
    (tmpdir / "pyproject.toml").write_text("some text", encoding="utf8")
    with shared.set_directory(tmpdir):
        root = shared.get_project_root()
    assert root == tmpdir


def test_get_project_root_from_subdir(tmpdir: Path):
    """Can get project root from sub folder"""
    (tmpdir / "pyproject.toml").write_text("some text", encoding="utf8")
    subfolder = tmpdir / "sub"
    subfolder.mkdir()
    with shared.set_directory(subfolder):
        root = shared.get_project_root()
    assert root == tmpdir


def test_get_project_root_not_exists(tmpdir: Path):
    """Raises ProjectRootNotFound if pyproject.toml not found"""
    subfolder = tmpdir / "sub"
    subfolder.mkdir()
    with shared.set_directory(subfolder):
        with pytest.raises(shared.ProjectRootNotFound):
            shared.get_project_root()
