"""Tests of the test cli commands"""

import pytest

from awesome_panel_cli.cli import test

# pylint: disable=redefined-outer-name


@pytest.fixture
def spy(mocker):
    """Patches the spy function"""
    return mocker.patch("awesome_panel_cli.cli.test.run")


def test_pylint(spy):
    """We can run pylint"""
    test.pylint()
    expected = ["pylint", "src/awesome_panel_cli", "tests", "-j", "0", "-f", "colorized"]
    spy.assert_called_once_with(command=expected)


def test_pylint_report(spy):
    """We can run pylint and generate a xml report"""
    test.pylint(report=True)
    expected = [
        "pylint",
        "src/awesome_panel_cli",
        "tests",
        "-j",
        "0",
        "-f",
        "colorized,pylint2junit.JunitReporter:test_results/pylint-results.xml",
    ]
    spy.assert_called_once_with(command=expected)


def test_mypy(spy):
    """We can run pylint"""
    test.mypy()
    expected = ["mypy", "src/awesome_panel_cli", "tests"]
    spy.assert_called_once_with(command=expected)


def test_mypy_report(spy):
    """We can run pylint and generate a xml report"""
    test.mypy(report=True)
    expected = [
        "mypy",
        "src/awesome_panel_cli",
        "tests",
        "--junit-xml",
        "test_results/mypy-results.xml",
    ]
    spy.assert_called_once_with(command=expected)


def test_bandit(spy):
    """We can run bandit"""
    test.bandit()
    expected = ["bandit", "-r", "./", "-c", "pyproject.toml", "--severity-level", "medium"]
    spy.assert_called_once_with(command=expected)


def test_bandit_pylint(spy):
    """We can run bandit and generate a xml report"""
    test.bandit(report=True)
    # pylint: disable=duplicate-code
    expected = [
        "bandit",
        "-r",
        "./",
        "-c",
        "pyproject.toml",
        "--severity-level",
        "medium",
        "-f",
        "xml",
        "-o",
        "test_results/bandit-results.xml",
    ]
    spy.assert_called_once_with(command=expected)


def test_pytest(spy):
    """We can run pytest"""
    test.pytest()
    expected = ["pytest", "tests"]
    spy.assert_called_once_with(command=expected)


def test_pytest_report(spy):
    """We can run pytest and generate a xml report"""
    test.pytest(report=True)
    expected = [
        "pytest",
        "tests",
        "--cov",
        "src",
        "--cov-report",
        "html:test_results/cov_html",
        "--junitxml",
        "test_results/pytest-results.xml",
        "--cov",
        "src/awesome_panel_cli",
        "--cov-report",
        "xml:test_results/coverage.xml",
    ]
    spy.assert_called_once_with(command=expected)


def test_all(mocker):
    """We can run all tests"""
    isort_ = mocker.patch("awesome_panel_cli.cli.test.autoformat.isort")
    autoflake_ = mocker.patch("awesome_panel_cli.cli.test.autoformat.autoflake")
    black_ = mocker.patch("awesome_panel_cli.cli.test.autoformat.black")
    pylint_ = mocker.patch("awesome_panel_cli.cli.test.pylint")
    mypy_ = mocker.patch("awesome_panel_cli.cli.test.mypy")
    bandit_ = mocker.patch("awesome_panel_cli.cli.test.bandit")
    pytest_ = mocker.patch("awesome_panel_cli.cli.test.pytest")

    test.all_()

    isort_.assert_called_once_with()
    autoflake_.assert_called_once_with()
    black_.assert_called_once_with()
    pylint_.assert_called_once_with(report=False)
    mypy_.assert_called_once_with(report=False)
    bandit_.assert_called_once_with(report=False)
    pytest_.assert_called_once_with(fast=False, report=False)


def test_all_fast(mocker):
    """We can run all tests fast"""
    isort_ = mocker.patch("awesome_panel_cli.cli.test.autoformat.isort")
    autoflake_ = mocker.patch("awesome_panel_cli.cli.test.autoformat.autoflake")
    black_ = mocker.patch("awesome_panel_cli.cli.test.autoformat.black")
    pylint_ = mocker.patch("awesome_panel_cli.cli.test.pylint")
    mypy_ = mocker.patch("awesome_panel_cli.cli.test.mypy")
    bandit_ = mocker.patch("awesome_panel_cli.cli.test.bandit")
    pytest_ = mocker.patch("awesome_panel_cli.cli.test.pytest")

    test.all_(fast=True)

    isort_.assert_called_once_with()
    autoflake_.assert_called_once_with()
    black_.assert_called_once_with()
    pylint_.assert_called_once_with(report=False)
    mypy_.assert_called_once_with(report=False)
    bandit_.assert_called_once_with(report=False)
    pytest_.assert_called_once_with(fast=True, report=False)


def test_all_report(mocker):
    """We can run all tests and create reports"""
    isort_ = mocker.patch("awesome_panel_cli.cli.test.autoformat.isort")
    autoflake_ = mocker.patch("awesome_panel_cli.cli.test.autoformat.autoflake")
    black_ = mocker.patch("awesome_panel_cli.cli.test.autoformat.black")
    pylint_ = mocker.patch("awesome_panel_cli.cli.test.pylint")
    mypy_ = mocker.patch("awesome_panel_cli.cli.test.mypy")
    bandit_ = mocker.patch("awesome_panel_cli.cli.test.bandit")
    pytest_ = mocker.patch("awesome_panel_cli.cli.test.pytest")

    test.all_(report=True)

    isort_.assert_called_once_with()
    autoflake_.assert_called_once_with()
    black_.assert_called_once_with()
    pylint_.assert_called_once_with(report=True)
    mypy_.assert_called_once_with(report=True)
    bandit_.assert_called_once_with(report=True)
    pytest_.assert_called_once_with(fast=False, report=True)
