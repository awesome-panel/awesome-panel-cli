"""Shared functionality for tasks"""
import logging
import os
import subprocess
from contextlib import contextmanager
from pathlib import Path
from typing import List

from rich.logging import RichHandler

from awesome_panel_cli import config

logger = logging.getLogger("panel-cli")


def logging_basic_config():
    """Configures the basic logging for the cli"""
    logging.basicConfig(
        level="INFO", format=config.LOGGING_FORMAT, datefmt="[%X]", handlers=[RichHandler()]
    )


def run(command: List[str]) -> bool:
    """Runs the specified command

    Args:
        command: A command list. For example ['pylint', 'src/awesome_panel_cli']

    Returns:
        True if the command was successfully executed. Otherwise False.
    """
    command_str = " ".join(command)
    logger.info("running: %s", command_str)
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        logger.error("failed: %s", command_str)
        return False
    return True


@contextmanager
def set_directory(path: Path):
    """Sets the cwd within the context

    Args:
        path (Path): The path to the cwd

    Yields:
        None
    """
    logger.info("running: cd %s", path)
    origin = Path().absolute()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(origin)


def is_project_root(path) -> bool:
    """Returns True if the path is a project root

    The criteriea is that it contains pyproject.toml
    """
    path = Path(path)
    return (path / "pyproject.toml").exists()


class ProjectRootNotFound(Exception):
    """The Project Root could not be found"""


def get_project_root():
    """Returns the root of the current project.

    It is the folder where `pyproject.toml` is located"""
    cwd = Path.cwd()
    for _ in range(0, 10):
        if is_project_root(cwd):
            return cwd
        cwd = cwd.parent
        logger.info("Searching for 'pyproject.toml' in %s", cwd)
    raise ProjectRootNotFound("Could not find project root")
