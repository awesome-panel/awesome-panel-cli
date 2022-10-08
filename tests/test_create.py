"""We can create Projects"""
from pathlib import Path

from awesome_panel_cli.cli import create
from awesome_panel_cli.shared import set_directory

# pylint: disable=protected-access


def test_create_project_file(tmpdir):
    """We can create the project files"""
    project_dir = create._create_project_files(output_dir=tmpdir, no_input=True)
    assert project_dir.name == "new-project"
    assert (project_dir / "src" / "new_project" / "__init__.py").exists()


def test_git_init(tmpdir):
    """We can git init a folder"""
    with set_directory(tmpdir):
        create._git_init()
        assert Path(".git").exists()
