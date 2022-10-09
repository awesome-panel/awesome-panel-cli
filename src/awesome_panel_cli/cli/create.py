"""Provides functionality for creating a new Panel project, app, component or examples folder."""
from __future__ import annotations

import os
import shutil
import tempfile
from pathlib import Path

import typer
from cookiecutter.main import cookiecutter
from rich.console import Console
from rich.markdown import Markdown

from awesome_panel_cli import config
from awesome_panel_cli.config import EXAMPLES, Example
from awesome_panel_cli.shared import logger, run, set_directory

app = typer.Typer()


def _create_project_files(
    output_dir="",
    no_input=False,
) -> Path:
    logger.info("Creating project files from cookiecutter template")
    project_dir = cookiecutter(
        str(config.PROJECT_TEMPLATE_ROOT), no_input=no_input, output_dir=output_dir
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

    You may optionally release your project to [Github](https://github.com/) by

    Creating a new, empty repository, i.e. with no `README.md`, `LICENSE` or `.gitignore` files.

    Then run

    ```bash
    git remote add origin https://github.com/<github-user>/{ source_dir.name }.git
    git push -f origin main
    ```
    """
    )
    console.print(markdown)


@app.command()
def project(virtual_env: bool = True):
    """Create new project"""
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


@app.command(name="app")
def app_(name: Example = Example.HELLO_WORLD):
    """Create a new app file in the current working directory

    Args:
        name: The name of an Awesome Panel example app. Defaults to 'hello_world'.
    """
    file_name = name.name.lower() + ".py"
    source = EXAMPLES / file_name
    target = Path.cwd()
    target = target / file_name
    if target.exists():
        logger.error("The file %s already exists!", target)
    else:
        shutil.copy(source, target)
        logger.info("created: %s", target)


@app.command()
def examples():
    """Creates an examples folder with all the Awesome Panel examples"""
    source = EXAMPLES
    target = Path.cwd() / "examples"

    if target.exists():
        logger.error("The folder %s already exists!", target)
    else:
        shutil.copytree(source, target)
        logger.info("created: %s", target)
        logger.info("serve with `panel serve examples/*.py`")


@app.command()
def component():
    """Create new component"""
    raise NotImplementedError()
