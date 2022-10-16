"""Main entrypoint for the Panel CLI"""


import typer

from awesome_panel_cli.cli import autoformat, build, create, release, test
from awesome_panel_cli.hello import (
    examples_awesome_panel_cli,
    examples_other,
    panel_serve,
)
from awesome_panel_cli.shared import logger, logging_basic_config

app = typer.Typer()
app.add_typer(autoformat.app, name="autoformat")
app.add_typer(build.app, name="build")
app.add_typer(create.app, name="create")
app.add_typer(release.app, name="release")
app.add_typer(test.app, name="test")


@app.command()
def examples(source: str = typer.Argument("awesome-panel-cli")):
    """Creates a folder with examples from the source repository."""
    if "awesome-panel-cli" in source:
        examples_awesome_panel_cli()
    elif source in ["panel", "holoviz/panel"]:
        logger.error("Panel is not supported. Use the `panel` cli to download the examples.")
    else:
        examples_other(source=source)


@app.command()
def hello(source: str = typer.Argument("awesome-panel-cli"), port: int = 5007):
    """Serves the examples from the source repository."""
    if source in ["panel", "holoviz/panel"]:
        logger.error(
            "Panel is not supported. Use the `panel` cli to download and serve the examples."
        )
    else:
        examples(source=source)
        panel_serve(source=source, port=port)


def run(func=app):
    """Main entrypoint for the Panel CLI"""
    logging_basic_config()
    func()
