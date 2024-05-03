from abc import ABC, abstractmethod

from mercury.models.rds.Task import Task
from mercury.models.rds.Data import Data


class AsyncRdsMapper(ABC):
    @abstractmethod
    async def insert_rds_data(self, rds_data: Data) -> None:
        """"""

    @abstractmethod
    async def find_rds_config_by_id(self, app_id: str) -> Task | None:
        """"""
