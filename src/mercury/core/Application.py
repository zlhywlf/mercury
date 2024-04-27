from abc import ABC, abstractmethod
from typing import Callable

from mercury.core.Engine import Engine


class Application(Engine, ABC):

    @property
    @abstractmethod
    def app(self) -> Callable:
        """"""
