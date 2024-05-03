from abc import ABC, abstractmethod

from mercury.models.rds.Data import Data
from mercury.models.rds.Task import Task


class AsyncRdsMapper(ABC):
    @abstractmethod
    async def insert_rds_data(self, rds_data: Data) -> None:
        """"""

    @abstractmethod
    async def find_rds_task_by_id(self, app_id: str) -> Task | None:
        """"""
