from abc import ABC, abstractmethod

from mercury.models.rds.Task import Task


class AsyncRdsService(ABC):
    @abstractmethod
    def get_data(self):
        """"""

    @abstractmethod
    async def get_rds_task(self, app_id: str) -> Task | None:
        """"""
