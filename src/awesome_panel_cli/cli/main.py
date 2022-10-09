"""Main entrypoint for the Panel CLI"""

import shutil

import typer

from awesome_panel_cli import config
from awesome_panel_cli.cli import autoformat, create, test
from awesome_panel_cli.shared import logging_basic_config
from awesome_panel_cli.shared import run as _run

app = typer.Typer()
app.add_typer(autoformat.app, name="autoformat")
app.add_typer(create.app, name="create")
app.add_typer(test.app, name="test")


@app.command()
def serve():
    """Serves the Awesome Panel example apps"""
    command = [
        "panel",
        "serve",
        "--num-threads",
        "4",
        str(config.REFERENCE_APPS) + "/*.py",
        "--glob",
    ]
    _run(command=command)


@app.command()
def intro(port: int = 8889):
    """Starts Jupyter Lab and serves the Awesome Panel 'Introduction to Panel' notebook."""
    tmpdir = config.REFERENCE_NOTEBOOKS / "tmp"
    if tmpdir.exists():
        try:
            tmpdir.rmdir()
            shutil.copytree(config.REFERENCE_NOTEBOOKS, tmpdir)
        except:  # pylint: disable=bare-except
            pass
    command = ["jupyter", "lab", "--port", str(port), "--notebook-dir", str(tmpdir)]
    _run(command=command)


def run(func=app):
    """Main entrypoint for the Panel CLI"""
    logging_basic_config()
    func()
