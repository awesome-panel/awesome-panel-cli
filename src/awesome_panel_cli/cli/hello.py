"""Serves the reference apps or notebooks"""
import shutil

import typer

from awesome_panel_cli import config
from awesome_panel_cli.shared import run

app = typer.Typer()


@app.command()
def apps():
    """Serves the Awesome Panel reference apps"""
    command = [
        "panel",
        "serve",
        "--num-threads",
        "4",
        str(config.REFERENCE_APPS) + "/*.py",
        "--glob",
    ]
    run(command=command)


@app.command()
def notebooks(port: int = 8889):
    """Serves the Awesome Panel reference notebooks in Jupyter lab."""
    tmpdir = config.REFERENCE_NOTEBOOKS / "tmp"
    if tmpdir.exists():
        try:
            tmpdir.rmdir()
            shutil.copytree(config.REFERENCE_NOTEBOOKS, tmpdir)
        except:  # pylint: disable=bare-except
            pass
    command = ["jupyter", "lab", "--port", str(port), "--notebook-dir", str(tmpdir)]
    run(command=command)
