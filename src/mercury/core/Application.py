from abc import ABC, abstractmethod
from typing import Callable

from mercury.core.Launch import Launch
from mercury.core.Setting import Setting


class Application(Launch, ABC):

    @property
    @abstractmethod
    def app(self) -> Callable:
        """"""

    @property
    @abstractmethod
    def setting(self) -> Setting:
        """"""

    @abstractmethod
    def add_route(self, path: str, endpoint: Callable, **kwargs) -> None:
        """"""

    @property
    @abstractmethod
    def platform(self) -> str:
        """"""
