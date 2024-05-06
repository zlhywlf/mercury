from abc import ABC, abstractmethod
from typing import Any

from mercury.models.rds.Content import Content
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
    async def handle_api(self, parent: Content, rds_task: Task) -> None:
        """"""

    @abstractmethod
    async def handle_table(self, parent: Content, rds_task: Task) -> None:
        """"""

    @abstractmethod
    async def handle_db(self, parent: Content, rds_task: Task) -> None:
        """"""

    @abstractmethod
    async def handle_subject(self, parent: Content, rds_task: Task) -> None:
        """"""

    @property
    @abstractmethod
    def content(self) -> Content:
        """"""
