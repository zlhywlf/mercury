from abc import ABC, abstractmethod
from typing import Any


class AsyncRdsService(ABC):
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
    async def handle_api(self) -> Any:
        """"""

    @abstractmethod
    async def handle_app(self) -> Any:
        """"""

    @abstractmethod
    async def handle_db(self) -> Any:
        """"""
