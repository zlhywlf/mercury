from abc import ABC, abstractmethod


class Controller(ABC):
    """"""

    @classmethod
    @abstractmethod
    def path(cls) -> list[str]:
        """"""
