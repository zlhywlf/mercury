from abc import ABC, abstractmethod

from mercury.core.Application import Application
from mercury.core.Setting import Setting


class Component(ABC):
    @abstractmethod
    def setup(self, app: Application, setting: Setting) -> None:
        """"""
