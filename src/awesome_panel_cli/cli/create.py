"""Provides functionality for creating a new Panel project, app, component or examples folder."""
from __future__ import annotations

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
    project_dir = cookiecutter(
        str(config.PROJECT_TEMPLATE_ROOT), no_input=no_input, output_dir=output_dir
    )
    return Path(project_dir)


def _git_init():
    run(["git", "init", "--initial-branch", "main"])
    run(["git", "add", "."])
    run(["git", "commit", "-a", "-m", "'Initial commit'"])


@app.command()
def project():
    """Create new project"""
    with tempfile.TemporaryDirectory() as tmpdir:
        source_dir = _create_project_files(output_dir=tmpdir)
        with set_directory(source_dir):
            _git_init()

        shutil.copytree(source_dir, source_dir.name)
    logger.info("Project %s was successfully created", source_dir.name)
    markdown = Markdown(
        f"""
    To finalize and test the installation please run

    ```bash
    cd {source_dir.name}
    python -m venv .venv
    source .venv/bin/activate
    pip install pip -U
    pip install -e .[dev]
    pn test all
    ```
    """
    )
    console = Console()
    console.print(markdown)


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
