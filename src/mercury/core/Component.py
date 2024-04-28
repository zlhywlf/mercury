from abc import ABC, abstractmethod

from mercury.core.Application import Application


class Component(ABC):
    @classmethod
    @abstractmethod
    def setup(cls, app: Application) -> None:
        """"""
