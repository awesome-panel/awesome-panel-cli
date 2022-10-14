"""Configuration"""
from enum import Enum
from pathlib import Path
from typing import List, Optional, Union

AUTOFLAKE_IMPORTS = "pytest,pandas,numpy,plotly,matplotlib,bokeh,dash,urllib3,param,panel,holoviews"
TEST_FOLDERS = "tests"
TEST_RESULTS_FOLDER = "test_results"
BANDIT_SEVERITY_LEVEL = "medium"
LOGGING_FORMAT = "%(message)s"

ROOT = Path(__file__).parent
TEMPLATES = ROOT / "templates"
REFERENCE_APPS = TEMPLATES / "apps"
REFERENCE_BINDER = TEMPLATES / ".binder"
REFERENCE_GITHUB = TEMPLATES / ".github"
REFERENCE_LICENSES = TEMPLATES / "licenses"
REFERENCE_NOTEBOOKS = TEMPLATES / "notebooks"
REFERENCE_PROJECT = TEMPLATES / "project"
REFERENCE_VIEWS = TEMPLATES / "views"
REFERENCE_WIDGETS = TEMPLATES / "widgets"


def _to_cwd_path(cwd: Optional[Union[str, Path]] = None) -> Path:
    """Returns the specified cwd as a Path

    Args:
        cwd (Optional[Union[str, Path]]): A current working directory. If cwd is None the Path.cwd()
            is returned. Default is None.

    Returns:
        Path: The cwd as a Path
    """
    if not cwd:
        return Path.cwd()
    return Path(cwd)


def _get_package_folder(cwd: Optional[Union[str, Path]] = None) -> Path:
    """Returns the package folder

    For example src, src/awesome_panel_cli, ...

    Args:
        cwd (Optional[Union[str, Path]], optional): The current working directory.
            Defaults to None.

    Returns:
        Path: The path to the package folder
    """
    cwd = _to_cwd_path(cwd)

    src = Path(cwd) / "src"
    for namespace in src.glob("*"):
        if namespace.is_dir() and not namespace.name.endswith(".egg-info"):
            return namespace

    return src


def _get_files() -> List[str]:
    cwd = Path.cwd()
    package_folder = _get_package_folder(cwd).relative_to(cwd)
    return [str(package_folder), "tests"]


_CWD = Path.cwd()
PACKAGE_FOLDER = _get_package_folder(_CWD).relative_to(_CWD)
FILES = _get_files()


class App(str, Enum):
    """Represents reference apps"""

    ALTAIR_STARTER = "altair"
    CROSS_FILTERING = "cross_filtering"
    HELLO_WORLD = "hello_world"
    STREAMING_INDICATORS = "streaming"


class Notebook(str, Enum):
    """Represents reference notebooks"""

    INTRODUCTION = "introduction"
    GETTING_STARTED = "getting_started"


class View(str, Enum):
    """Represents reference views

    A `View` is just a function. It can return a composite Panel component, output of a model or
    algorithm, Markdown, HTML and more. You can bind widgets and parameters to views.

    You can also make interactive, standalone components by combining a *view* with a *viewer*
    pane."""

    VIEW = "view"
    VIEW_HTML = "html"


class Widget(str, Enum):
    """Represents reference components"""

    VIEWER = "viewer"


class License(str, Enum):
    """Represents licenses"""

    MIT = "mit"
