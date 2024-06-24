"""Application config.

Copyright (c) 2023-present 善假于PC也 (zlhywlf) .
"""

from starlette.config import Config


class MercuryConfig:
    """Application config."""

    def __init__(self) -> None:
        """Init."""
        self._config = Config(env_prefix="MERCURY_")
