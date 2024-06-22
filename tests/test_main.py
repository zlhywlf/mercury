"""Application tests.

Copyright (c) 2023-present 善假于PC也 (zlhywlf).
"""

from mercury.__main__ import main


def test_main() -> None:
    """Test main."""
    assert main.__name__ == "main"
