"""Application launcher.

Copyright (c) 2023-present 善假于PC也 (zlhywlf) .
"""

from typing import Any

import click

from mercury._version import version


@click.command()
@click.option("-V", "--version", is_flag=True, help="Show program's version number and exit")
def main(**kwargs: Any) -> None:
    """Launcher."""
    if kwargs["version"]:
        print(version)  # noqa: T201
        return
