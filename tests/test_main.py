"""Test the main run function"""
from awesome_panel_cli.cli.main import run

# pylint: disable=redefined-outer-name


def _pass_func():
    pass


def test_run():
    """We can run the main run function"""
    run(_pass_func)
