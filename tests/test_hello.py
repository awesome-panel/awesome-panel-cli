"""Test the main run function"""
import pytest
from typer.testing import CliRunner

from awesome_panel_cli.cli.main import app
from awesome_panel_cli.hello import _get_examples_dir
from awesome_panel_cli.shared import set_directory

# pylint: disable=redefined-outer-name


runner = CliRunner()


@pytest.fixture
def spy(mocker):
    """Patches the spy function"""
    return mocker.patch("awesome_panel_cli.hello.run")


def test_hello(spy, tmpdir):
    """We can easily panel serve some examples"""
    with set_directory(tmpdir):
        result = runner.invoke(app, ["hello"])
        assert result.exit_code == 0
        assert _get_examples_dir("awesome-panel-cli").exists()
        spy.assert_called_once()


@pytest.mark.slow()
def test_hello_panel_chemistry(spy, tmpdir):
    """We can easily panel serve some panel-chemistry examples"""
    with set_directory(tmpdir):
        result = runner.invoke(app, ["hello", "panel-chemistry"])
        assert result.exit_code == 0
        assert _get_examples_dir("panel-chemistry").exists()
        spy.assert_called_once()
        assert {"panel", "serve"}.issubset(set(spy.call_args.args[0]))
