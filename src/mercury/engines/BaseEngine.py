from abc import ABC
from typing import Callable

from mercury.core.Engine import Engine


class BaseEngine(Engine, ABC):
    platform_type = []
    use_for_debug = False

    def __init__(self, app: Callable):
        self._app = app
