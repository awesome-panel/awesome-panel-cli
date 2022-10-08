"""Module of test tasks to validate the quality of the code.
"""
import pathlib
import time
from typing import Optional, Union

import typer

from awesome_panel_cli import config
from awesome_panel_cli.shared import logger, run

from . import autoformat

app = typer.Typer()


def _create_test_results_folder(
    cwd: Optional[Union[str, pathlib.Path]] = None, name=config.TEST_RESULTS_FOLDER
):
    """Creates a subfolder with the specific name in the cwd folder"""
    if not cwd:
        cwd = pathlib.Path.cwd()
    else:
        cwd = pathlib.Path(cwd)

    pathlib.Path(cwd / name).mkdir(exist_ok=True)


@app.command()
def bandit(report: bool = False):
    """Runs Bandit the security linter from PyCQA.

    Args:
        report (bool, optional): If True an xml report will be created. Defaults to False.
    """
    command = [
        "bandit",
        "-r",
        "./",
        "-c",
        "pyproject.toml",
        "--severity-level",
        config.BANDIT_SEVERITY_LEVEL,
    ]

    if report:
        command.extend(
            [
                "-f",
                "xml",
                "-o",
                f"{config.TEST_RESULTS_FOLDER}/bandit-results.xml",
            ]
        )
    return run(command=command)


@app.command()
def pytest(
    fast: bool = False,
    test_files: str = config.TEST_FOLDERS,
    report: bool = False,
    pdb: bool = False,
):
    """Runs Pytest to identify failing tests

    Keyword Arguments:
        root_dir {str} -- The directory from which to run the tests
        test_files {str} -- A space separated list of folders and files to test. (default: {'tests})
        fast {bool} -- If True tests marked slow will not be
            run. (default: False)
        report {bool} -- If True test reports will be generated in the test_results
            folder. (default: False)
    """
    # Build the command_string
    command = [
        "pytest",
        test_files,
    ]
    if fast:
        command.extend(
            [
                "-m",
                "'not slow'",
            ]
        )
    if report:
        _create_test_results_folder()
        command.extend(
            [
                "--cov",
                "src",
                "--cov-report",
                f"html:{config.TEST_RESULTS_FOLDER}/cov_html",
            ]
        )
        command.extend(
            [
                "--junitxml",
                f"{config.TEST_RESULTS_FOLDER}/pytest-results.xml",
                "--cov",
                str(config.PACKAGE_FOLDER),
                "--cov-report",
                "xml:test_results/coverage.xml",
            ]
        )
    if pdb:
        command.extend(["--pdb"])

    # Run the command_string
    return run(command=command)


@app.command()
def pylint(report: bool = False):
    """Runs Pylint (linter) on all .py files recursively to identify coding errors

    Arguments:
        files {string} -- A space separated list of files and folders to lint
        report (bool, optional): If True an xml report will be created. Defaults to False.

    """
    command = [
        "pylint",
        *config.FILES,
        "-j",
        "0",
        "-f",
    ]
    output_format = "colorized"
    if report:
        _create_test_results_folder()
        output_format += (
            f",pylint2junit.JunitReporter:{config.TEST_RESULTS_FOLDER}/pylint-results.xml"
        )
    command.append(output_format)
    return run(command=command)


@app.command()
def mypy(report: bool = False):
    """Runs mypy on all .py files recursively to identify type errors

    Arguments:
        files {string} -- A space separated list of files and folders to lint
        report (bool, optional): If True an xml report will be created. Defaults to False.

    """
    command = [
        "mypy",
        *config.FILES,
    ]
    if report:
        _create_test_results_folder()
        command.extend(
            [
                "--junit-xml",
                f"{config.TEST_RESULTS_FOLDER}/mypy-results.xml",
            ]
        )
    return run(command=command)


@app.command(name="all")
def all_(
    fast: bool = False,
    report: bool = False,
):
    """Runs all autoformatting and tests

    Arguments:
        fast {bool} -- If True tests marked slow will not be
            run. (default: False)
        report {bool} -- If True test reports will be generated in the test_results
            folder. (default: False)
    """
    start = time.time()
    failed = []

    if not autoformat.isort():
        failed.append("isort")
    if not autoformat.autoflake():
        failed.append("autoflake")
    if not autoformat.black():
        failed.append("black")
    if not pylint(report=report):
        failed.append("pylint")
    if not mypy(report=report):
        failed.append("mypy")
    if not bandit(report=report):
        failed.append("bandit")
    if not pytest(fast=fast, report=report):
        failed.append("pytest")
    duration = int(time.time() - start)
    if failed:
        logger.error("finished with errors in %ss: %s", duration, failed)
    else:
        logger.info("finished with success in %ss", duration)


@app.command()
def show():
    """Opens a browser with the test coverage results"""
    command = [
        "start",
        f"{config.TEST_RESULTS_FOLDER}/cov_html/index.html",
    ]
    run(command=command)
