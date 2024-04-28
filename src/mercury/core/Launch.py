from abc import ABC, abstractmethod


class Launch(ABC):
    @abstractmethod
    def launch(self) -> None:
        """"""
