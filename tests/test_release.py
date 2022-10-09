"""We can release the project including the python package"""
import pytest

from awesome_panel_cli.cli import release

# pylint: disable=redefined-outer-name


@pytest.fixture
def spy(mocker):
    """Patches the spy function"""
    return mocker.patch("awesome_panel_cli.cli.release.run")


def test_python_package(spy):
    """We can build a python package"""
    version = "1.0.0"
    release.python_package(version=version)
    expected = ["python", "-m", "twine", "upload", f"dist/*{version}*"]
    spy.assert_called_once_with(command=expected)


def test_python_package_test(spy):
    """We can build a python package"""
    version = "1.0.0"
    release.python_package(version=version, test=True)
    expected = [
        "python",
        "-m",
        "twine",
        "upload",
        f"dist/*{version}*",
        "--repository",
        "testpypi",
    ]
    spy.assert_called_once_with(command=expected)
