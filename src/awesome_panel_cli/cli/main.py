"""Main entrypoint for the Panel CLI"""


import typer

from awesome_panel_cli.cli import autoformat, build, create, hello, release, test
from awesome_panel_cli.shared import logging_basic_config

app = typer.Typer()
app.add_typer(autoformat.app, name="autoformat")
app.add_typer(build.app, name="build")
app.add_typer(create.app, name="create")
app.add_typer(hello.app, name="hello")
app.add_typer(release.app, name="release")
app.add_typer(test.app, name="test")


def run(func=app):
    """Main entrypoint for the Panel CLI"""
    logging_basic_config()
    func()
