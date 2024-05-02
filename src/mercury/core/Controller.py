from abc import ABC, abstractmethod


class Controller(ABC):
    """"""

    @classmethod
    @abstractmethod
    def paths(cls) -> list[str]:
        """"""

    @classmethod
    @abstractmethod
    def middlewares[T](cls) -> list[T]:
        """"""
