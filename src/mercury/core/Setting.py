from abc import ABC, abstractmethod


class Setting(ABC):
    @property
    @abstractmethod
    def debug(self) -> bool:
        """"""

    @property
    @abstractmethod
    def project_name(self) -> str:
        """"""

    @property
    @abstractmethod
    def app_key(self) -> str:
        """"""

    @property
    @abstractmethod
    def mongo(self) -> str:
        """"""
