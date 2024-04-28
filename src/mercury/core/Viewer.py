from abc import ABC, abstractmethod
from mercury.core.Application import Application


class Viewer(ABC):
    """"""

    @classmethod
    @abstractmethod
    def path(cls) -> str:
        """"""

    @classmethod
    @abstractmethod
    def setup(cls, app: Application) -> None:
        """"""
