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

    @property
    @abstractmethod
    def mongo(self) -> str:
        """"""

    @property
    @abstractmethod
    def rds_task_table_name(self) -> str:
        """"""

    @property
    @abstractmethod
    def rds_data_table_name(self) -> str:
        """"""
