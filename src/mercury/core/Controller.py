from abc import ABC, abstractmethod

from mercury.core.Application import Application


class Controller(ABC):
    """"""

    @classmethod
    @abstractmethod
    def path(cls) -> str:
        """"""

    @classmethod
    @abstractmethod
    def setup(cls, application: Application) -> None:
        """"""
