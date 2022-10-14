"""Provides functionality for creating a new Panel project, app, component or examples folder."""
from __future__ import annotations

import os
import shutil
import tempfile
from enum import Enum
from pathlib import Path

import typer
from cookiecutter.main import cookiecutter
from rich.console import Console
from rich.markdown import Markdown

from awesome_panel_cli import config, shared
from awesome_panel_cli.shared import logger, run, set_directory

app = typer.Typer()


def _create_project_files(
    output_dir="",
    no_input=False,
) -> Path:
    logger.info("Creating project files from cookiecutter template")
    project_dir = cookiecutter(
        str(config.REFERENCE_PROJECT), no_input=no_input, output_dir=output_dir
    )
    return Path(project_dir)


def _git_init():
    logger.info("Initializing git")
    run(["git", "init", "--initial-branch", "main"])
    run(["git", "add", "."])
    run(["git", "commit", "-a", "-m", "'Initial commit'"])


def _get_python_path() -> str:
    if os.name == "nt":
        return str(Path(".venv/Scripts/python"))
    return str(Path(".venv/bin/python"))


def _get_python_env_activate_command() -> str:
    if os.name == "nt":
        return ".venv/Scripts/activate"
    return "source .venv/bin/activate"


def _create_virtual_environment():
    logger.info("Creating the virtual environment")
    run(["python", "-m", "venv", ".venv"])
    run([_get_python_path(), "-m", "pip", "install", "pip", "-U"])
    run([_get_python_path(), "-m", "pip", "install", "-e", ".[dev]", "-U"])


def _print_comments(source_dir):
    console = Console()
    markdown = Markdown(
        f"""
    You may try out your new repository by running

    ```bash
    cd {source_dir}
    {_get_python_env_activate_command()}
    pn test all
    pn --help
    panel serve apps/app.py --autoreload
    ```

    If you want to serve the Awesome Panel reference apps or notebooks you will need to install

    ```bash
    pip install awesome-panel-cli[all] -U
    ```

    If you want to release your project to [Github](https://github.com/) you can do so by

    Creating a new, empty repository, i.e. with no `README.md`, `LICENSE` or `.gitignore` files.

    Then running

    ```bash
    git remote add origin https://github.com/<github-user>/{ source_dir.name }.git
    git push -f origin main
    pn create github-actions
    ```
    """
    )
    console.print(markdown)


@app.command()
def project(virtual_env: bool = True):
    """Creates a new best practice python project for developing data apps

    This will create a new project in a subfolder of the current directory.

    This includes a virtual environment, a pyproject.toml file, a starter apps/app.py file,
    a starter tests/test_hello.py file and more
    """
    source_dir: None | Path = None
    with tempfile.TemporaryDirectory() as tmpdir:
        try:
            tmp_source_dir = _create_project_files(output_dir=tmpdir)
            with set_directory(tmp_source_dir):
                _git_init()
            shutil.copytree(tmp_source_dir, tmp_source_dir.name)

            source_dir = Path(tmp_source_dir.name)
            if virtual_env:
                with set_directory(source_dir):
                    _create_virtual_environment()
            _print_comments(source_dir=source_dir)

            logger.info("The Project %s was successfully created", source_dir.name)
        except Exception as ex:  # pylint: disable=broad-except
            if isinstance(source_dir, Path) and source_dir.exists():
                shutil.rmtree(source_dir)
            logger.exception("The Project was NOT created", exc_info=ex)


def _copy_file(name: Enum, source_dir: Path, postfix: str = ".py"):
    file_name = name.name.lower() + postfix
    source = source_dir / file_name
    target = Path.cwd()
    target = target / file_name
    if target.exists():
        logger.error("The file %s already exists!", target)
    else:
        shutil.copy(source, target)
        logger.info("created: %s", target)


def _copy_tree(source, target):
    if target.exists():
        logger.error("The folder %s already exists! Please delete it first and rerun.", target)
        return

    try:
        shutil.copytree(source, target)
        logger.info("created: %s", target)
    except Exception as ex:  # pylint: disable=broad-except
        logger.exception("Could not create %s folder", target, exc_info=ex)


@app.command(name="app")
def app_(name: config.App = config.App.HELLO_WORLD):
    """Creates a new app file in the current working directory

    Args:
        name: The name of an reference app. Defaults to 'hello_world'.
    """
    _copy_file(
        name=name,
        source_dir=config.REFERENCE_APPS,
    )


@app.command()
def notebook(name: config.Notebook = config.Notebook.INTRODUCTION):
    """Creates a new notebook file in the current working directory

    Args:
        name: The name of an reference notebook. Defaults to 'introduction'.
    """
    _copy_file(name, config.REFERENCE_NOTEBOOKS, postfix=".ipynb")


@app.command()
def view(name: config.View = config.View.VIEW):
    """Creates a new view file in the current working directory

    A view is just a function returning some object that Panel can display.

    Args:
        name: The name of a reference view. Defaults to 'view'.
        example: If True the file generated contains a detailed example
    """
    _copy_file(
        name,
        config.REFERENCE_VIEWS,
    )


@app.command()
def widget(name: config.Widget = config.Widget.VIEWER, example: bool = False):
    """Creates a new widget file in the current working directory

    A widget is a Parameterized Class with a `value` parameter. You can set the value. The value
    can change when the user interacts with the widget.

    Args:
        name: The name of a reference widget. Defaults to 'viewer'.
        example: If True the file generated contains a detailed example
    """
    if example:
        prefix = "_example.py"
    else:
        prefix = ".py"
    _copy_file(name, config.REFERENCE_WIDGETS, prefix)


@app.command()
def examples(target="examples"):
    """Creates an examples folder with all the Awesome Panel reference examples"""
    _examples = Path.cwd() / target
    if _examples.exists():
        logger.error("The folder %s already exists! Please delete it first and rerun.", _examples)
        return

    try:
        for _source, _target_dir in [
            (config.REFERENCE_APPS, "apps"),
            (config.REFERENCE_NOTEBOOKS, "notebooks"),
            (config.REFERENCE_VIEWS, "views"),
            (config.REFERENCE_WIDGETS, "widgets"),
        ]:
            _target = _examples / _target_dir

            shutil.copytree(_source, _target)
        logger.info("created: %s", _target)
    except Exception as ex:  # pylint: disable=broad-except
        if _examples.exists():
            shutil.rmtree(_examples)
            logger.exception("Could not create examples folder", exc_info=ex)


@app.command()
def github_actions():
    """Populates the .github folder"""
    _copy_tree(
        source=config.REFERENCE_GITHUB,
        target=shared.get_project_root() / ".github",
    )


@app.command()
def binder():
    """Populates the .binder folder"""
    _copy_tree(
        source=config.REFERENCE_BINDER,
        target=shared.get_project_root() / ".binder",
    )


@app.command()
def license_(name: config.License = config.License.MIT):
    """Creates a new license file in the project root.

    Args:
        name: The name of the license. Defaults to 'MIT'.
    """
    file_name = name.name.lower()
    source = config.REFERENCE_LICENSES / file_name
    target = shared.get_project_root()
    target = target / "LICENSE"
    if target.exists():
        logger.error("The file %s already exists!", target)
    else:
        shutil.copy(source, target)
        logger.info("created: %s", target)
