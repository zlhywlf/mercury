from abc import ABC, abstractmethod
from mercury.core.Launch import Launch


class Engine(Launch, ABC):
    @classmethod
    @abstractmethod
    def platforms(cls) -> list[str]:
        """"""

    @classmethod
    @abstractmethod
    def debug(cls) -> bool:
        """"""
