"""Tests of the autoformat cli commands"""

import pytest

from awesome_panel_cli.cli import autoformat


# pylint: disable=redefined-outer-name
@pytest.fixture
def spy(mocker):
    """Patches the spy function"""
    return mocker.patch("awesome_panel_cli.cli.autoformat.run")


def test_isort(spy):
    """We can spy isort"""
    autoformat.isort()
    expected = ["isort", "src/awesome_panel_cli", "tests"]
    spy.assert_called_once_with(command=expected)


def test_autoflake(spy):
    """We can spy autoflake"""
    autoformat.autoflake()
    expected = [
        "autoflake",
        "--imports",
        "pytest,pandas,numpy,plotly,matplotlib,bokeh,dash,urllib3,param,panel,holoviews",
        "--in-place",
        "--recursive",
        "src/awesome_panel_cli",
        "tests",
    ]
    spy.assert_called_once_with(command=expected)


def test_black(spy):
    """We can spy black"""
    autoformat.black()
    expected = ["black", "src/awesome_panel_cli", "tests", "-l", "100"]
    spy.assert_called_once_with(command=expected)


def test_all(mocker):
    """We can run all autoformats"""
    isort_ = mocker.patch("awesome_panel_cli.cli.test.autoformat.isort")
    autoflake_ = mocker.patch("awesome_panel_cli.cli.test.autoformat.autoflake")
    black_ = mocker.patch("awesome_panel_cli.cli.test.autoformat.black")

    autoformat.all_()

    isort_.assert_called_once_with()
    autoflake_.assert_called_once_with()
    black_.assert_called_once_with()
