from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def launch(self) -> None:
        """"""
