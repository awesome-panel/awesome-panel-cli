"""Functionality for other awesome-panel packages to enable examples and hello cli commands"""
from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

from gitdir.gitdir import download

from awesome_panel_cli import config
from awesome_panel_cli.shared import logger, run, set_directory


def _get_full_source(source: str) -> str:
    if not "/" in source:
        source = "awesome-panel/" + source
    return source


def _get_examples_dir(source: str) -> Path:
    source = _get_full_source(source)
    return Path("examples") / source


def _get_examples_url(source: str) -> str:
    source = _get_full_source(source)
    return f"https://github.com/{source}/tree/main/examples"


def examples_other(source: str):
    """Downloads the examples folder from the source repository

    If the source contains only the repository name we will assume by default that the github user
    is awesome-panel. I.e. the source 'panel-highcharts' will point to
    'awesome-panel/panel-highcharts'.

    Args:
        source: A source repository. For example `panel-highcharts` or
            `awesome-panel/panel-highcharts`.
    """
    output_dir = _get_examples_dir(source).absolute()
    if output_dir.exists():
        logger.info("Removing %s", output_dir)
        shutil.rmtree(output_dir)
    output_dir.parent.mkdir(exist_ok=True, parents=True)

    examples_url = _get_examples_url(source)
    with tempfile.TemporaryDirectory() as tmpdir:
        with set_directory(tmpdir):
            download(examples_url)

            tmp_src = examples_url.split("main/")[-1]
            shutil.copytree(tmp_src, output_dir)
            logger.info("Created %s", output_dir)


def examples_awesome_panel_cli():
    """Creates the examples/awesome-panel-cli folder"""
    output_dir = _get_examples_dir(source="awesome-panel-cli")

    if output_dir.exists():
        shutil.rmtree(output_dir)
    source = [
        config.REFERENCE_APPS,
        config.REFERENCE_NOTEBOOKS,
        config.REFERENCE_VIEWS,
        config.REFERENCE_WIDGETS,
    ]
    for src in source:
        dst = output_dir / src.name
        shutil.copytree(src, dst)
        logger.info("Created %s", dst)


def panel_serve(source: str = "awesome-panel-cli", port: int = 5007):
    """Serves all .py and .ipynb in the examples folder of the source

    Args:
        source: _description_. Defaults to "awesome-panel-cli".
        port: _description_. Defaults to 5007.
    """
    output_dir = _get_examples_dir(source)
    scripts = map(str, Path(output_dir).rglob("*.py"))
    notebooks = map(str, Path(output_dir).rglob("*.ipynb"))
    # We don't use threads currently due to https://github.com/holoviz/panel/issues/4010
    # "--num-threads", "4",
    run(["panel", "serve", "--port", str(port), *scripts, *notebooks])
