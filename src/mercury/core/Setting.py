from abc import ABC, abstractmethod


class Setting(ABC):
    @property
    @abstractmethod
    def is_debug(self) -> bool:
        """"""
