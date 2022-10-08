"""Collection of commands for autoformatting"""
import typer

from awesome_panel_cli import config
from awesome_panel_cli.shared import run

app = typer.Typer()


@app.command()
def autoflake():
    """Runs autoflake to remove unused imports on all .py files recursively"""
    command = [
        "autoflake",
        "--imports",
        config.AUTOFLAKE_IMPORTS,
        "--in-place",
        "--recursive",
        *config.FILES,
    ]
    run(
        command=command,
    )
    return True


@app.command()
def isort():
    """Runs isort to sort all imports in all .py files recursively"""
    command = [
        "isort",
        *config.FILES,
    ]
    run(command=command)
    return True


@app.command()
def black():
    """Runs black to autoformat all .py files recursively"""
    command = ["black", *config.FILES, "-l", "100"]
    run(command=command)
    return True


@app.command(name="all")
def all_():
    """Runs autoflake, isort and black"""
    isort()
    autoflake()
    black()
