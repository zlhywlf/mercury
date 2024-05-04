from abc import ABC, abstractmethod
from typing import Any

from mercury.models.rds.Task import Task


class RdsService(ABC):
    @abstractmethod
    async def get_data(self) -> Any:
        """"""

    @abstractmethod
    async def get_rds_task(self) -> bool:
        """"""

    @property
    @abstractmethod
    def app_id(self) -> str | None:
        """"""

    @abstractmethod
    async def handle_api(self, params: dict, rds_task: Task) -> Any:
        """"""

    @abstractmethod
    async def handle_app(self, params: dict, rds_task: Task) -> Any:
        """"""

    @abstractmethod
    async def handle_db(self, params: dict, rds_task: Task) -> Any:
        """"""
