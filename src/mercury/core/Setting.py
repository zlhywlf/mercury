from abc import ABC, abstractmethod


class Setting(ABC):
    @property
    @abstractmethod
    def is_debug(self) -> bool:
        """"""

    @property
    @abstractmethod
    def rds_key(self) -> str:
        """"""
