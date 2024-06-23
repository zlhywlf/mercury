"""Tests config.

Copyright (c) 2023-present 善假于PC也 (zlhywlf).
"""

import pytest
from click.testing import CliRunner


@pytest.fixture(scope="module")
def cli_runner() -> CliRunner:
    """CliRunner.

    Returns: CliRunner

    """
    return CliRunner()
