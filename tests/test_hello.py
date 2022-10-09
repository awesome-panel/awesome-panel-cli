"""Test the main run function"""
import pytest

from awesome_panel_cli import config
from awesome_panel_cli.cli import hello

# pylint: disable=redefined-outer-name


@pytest.fixture
def spy(mocker):
    """Patches the spy function"""
    return mocker.patch("awesome_panel_cli.cli.hello.run")


def test_show(spy):
    """We can showcase some panel apps"""
    hello.apps()
    expected = [
        "panel",
        "serve",
        "--num-threads",
        "4",
        str(config.REFERENCE_APPS) + "/*.py",
        "--glob",
    ]
    spy.assert_called_once_with(command=expected)


def test_intro(spy):
    """We can start an introduction notebook"""
    hello.notebooks()
    expected = [
        "jupyter",
        "lab",
        "--port",
        "8889",
        "--notebook-dir",
        str(config.REFERENCE_NOTEBOOKS / "tmp"),
    ]
    spy.assert_called_once_with(command=expected)
