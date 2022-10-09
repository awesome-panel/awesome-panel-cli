"""We can build the project including the python package"""
import typer

from awesome_panel_cli.shared import logger, run

app = typer.Typer()


@app.command(name="package")
def python_package():
    """Builds the python package"""
    command = ["python", "-m", "build"]
    run(command=command)
    logger.info("Package build finished with success")
