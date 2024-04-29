from abc import ABC, abstractmethod

from mercury.core.Application import Application
from mercury.core.Launch import Launch


class BaseEngine(Launch, ABC):

    def __init__(self, application: Application) -> None:
        self._application = application

    @classmethod
    @abstractmethod
    def platforms(cls) -> list[str]:
        """"""

    @classmethod
    @abstractmethod
    def debug(cls) -> bool:
        """"""
