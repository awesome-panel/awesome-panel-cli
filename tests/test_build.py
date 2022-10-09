"""Tests of the build cli commands"""

import pytest

from awesome_panel_cli.cli import build

# pylint: disable=redefined-outer-name


@pytest.fixture
def spy(mocker):
    """Patches the spy function"""
    return mocker.patch("awesome_panel_cli.cli.build.run")


def test_python_package(spy):
    """We can build a python package"""
    build.python_package()
    expected = ["python", "-m", "build"]
    spy.assert_called_once_with(command=expected)
