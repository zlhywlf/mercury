from abc import ABC, abstractmethod
from typing import Callable

from mercury.core.Engine import Engine
from mercury.core.Setting import Setting


class Application(Engine, ABC):

    @property
    @abstractmethod
    def app(self) -> Callable:
        """"""

    @property
    @abstractmethod
    def setting(self) -> Setting:
        """"""
