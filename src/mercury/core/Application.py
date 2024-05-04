from abc import ABC, abstractmethod

from mercury.core.Launch import Launch
from mercury.core.Setting import Setting


class Application(Launch, ABC):

    def __init__(self, **kwargs): ...

    def __call__(self) -> None: ...

    # @property
    # @abstractmethod
    # def instance(self) -> Callable:
    #     """"""

    @property
    @abstractmethod
    def setting(self) -> Setting:
        """"""

    # @abstractmethod
    # def add_route(self, path: str, endpoint: Callable, **kwargs) -> None:
    #     """"""

    @property
    @abstractmethod
    def platform(self) -> str:
        """"""
