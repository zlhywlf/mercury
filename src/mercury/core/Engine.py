from abc import ABC, abstractmethod
from typing import Self

from mercury.core.Application import Application
from mercury.core.Launch import Launch


class Engine(Launch, ABC):
    @classmethod
    @abstractmethod
    def platforms(cls) -> list[str]:
        """"""

    @classmethod
    @abstractmethod
    def is_run_for_debug(cls) -> bool:
        """"""

    @abstractmethod
    def set_application(self, application: Application) -> Self:
        """"""
