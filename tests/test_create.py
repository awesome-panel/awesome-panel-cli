"""We can create Projects"""
from pathlib import Path

import pytest

from awesome_panel_cli import config
from awesome_panel_cli.cli import create
from awesome_panel_cli.shared import set_directory

# pylint: disable=protected-access

@pytest.fixture()
def tmp_project_dir(tmpdir):
    Path(tmpdir / "pyproject.toml").write_text("something", encoding="utf8")
    return tmpdir


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


def test_create_app(tmpdir):
    """We can create an app"""
    source = config.App.ALTAIR_STARTER
    target = Path(source.name.lower() + ".py")
    with set_directory(tmpdir):
        create.app_(source)
        assert target.exists()


def test_create_notebook(tmpdir):
    """We can create a notebook"""
    source = config.Notebook.GETTING_STARTED
    target = Path(source.name.lower() + ".ipynb")
    with set_directory(tmpdir):
        create.notebook(source)
        assert target.exists()


def test_create_view(tmpdir):
    """We can create a component"""
    source = config.View.VIEW
    target = Path(source.name.lower() + ".py")
    with set_directory(tmpdir):
        create.view(source)
        assert target.exists()


def test_create_widget(tmpdir):
    """We can create a widget"""
    source = config.Widget.VIEWER
    target = Path(source.name.lower() + ".py")
    with set_directory(tmpdir):
        create.widget(source)
        assert target.exists()


def test_create_widget_example(tmpdir):
    """We can create a widget example"""
    source = config.Widget.VIEWER
    target = Path(source.name.lower() + "_example.py")
    with set_directory(tmpdir):
        create.widget(source, example=True)
        assert target.exists()


def test_create_examples(tmpdir):
    """We can create an examples folder"""
    with set_directory(tmpdir):
        create.examples()
        examples = Path("examples")
        assert (examples / "apps" / "hello_world.py").exists()
        assert (examples / "notebooks" / "introduction.ipynb").exists()
        assert (examples / "views" / "view_html.py").exists()
        assert (examples / "widgets" / "viewer.py").exists()


def test_create_github(tmpdir):
    """We can create a .github actions folder"""
    with set_directory(tmpdir):
        Path(tmpdir / "pyproject.toml").write_text("something", encoding="utf8")
        create.github_actions()
        github = Path(".github")
        assert (github / "workflows" / "tests.yaml").exists()


def test_create_binder(tmpdir):
    """We can create a .binder actions folder"""
    with set_directory(tmpdir):
        Path(tmpdir / "pyproject.toml").write_text("something", encoding="utf8")
        create.binder()
        github = Path(".binder")
        assert (github / "requirements.txt").exists()

def test_create_license(tmp_project_dir):
    """We can create a license"""
    source = config.License.MIT
    target = Path("LICENSE")
    with set_directory(tmp_project_dir):
        create.license(source)
        assert target.exists()
