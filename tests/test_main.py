"""Application tests.

Copyright (c) 2023-present 善假于PC也 (zlhywlf).
"""

import pytest
from click.testing import CliRunner
from mercury.__main__ import main

# noinspection PyProtectedMember
from mercury._version import version


@pytest.mark.parametrize(
    "command",
    [
        pytest.param("-V", id="-V"),
        pytest.param("--version", id="--version"),
    ],
)
def test_main(cli_runner: CliRunner, command: str) -> None:
    """Test main."""
    # noinspection PyTypeChecker
    result = cli_runner.invoke(main, [command])
    assert result.exit_code == 0
    assert version in result.output
