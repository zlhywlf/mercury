from abc import ABC, abstractmethod

from mercury.models.RdsConfig import RdsConfig
from mercury.models.RdsData import RdsData


class AsyncRdsMapper(ABC):
    @abstractmethod
    async def insert_rds_data(self, rds_data: RdsData) -> None:
        """"""

    @abstractmethod
    async def find_rds_config_by_id(self, app_id: str) -> RdsConfig | None:
        """"""
