"""Serves the reference apps or notebooks"""
import typer

from awesome_panel_cli.shared import logger, run

app = typer.Typer()


@app.command(name="package")
def python_package(version: str, test: bool = False):
    """Release the Package to pypi

    Args:
        version: The version to upload, for example '0.1.0'.
        test: If True releases to test pypi. Defaults to False.
    """
    command = ["python", "-m", "twine", "upload", f"dist/*{version}*"]
    if test:
        command.extend(
            [
                "--repository",
                "testpypi",
            ]
        )
    run(command=command)
    logger.info("Package released with with success")
