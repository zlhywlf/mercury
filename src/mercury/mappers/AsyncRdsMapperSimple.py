from typing import override

from motor.motor_asyncio import AsyncIOMotorDatabase

from mercury.core.mappers.AsyncRdsMapper import AsyncRdsMapper
from mercury.models.RdsConfig import RdsConfig
from mercury.models.RdsData import RdsData


class AsyncRdsMapperSimple(AsyncRdsMapper):
    """"""

    def __init__(self, db: AsyncIOMotorDatabase):
        self._rds_data = db["rds_data"]
        self._rds_config = db["rds_config"]
        self._rds_api = db["rds_api"]

    @override
    async def insert_rds_data(self, rds_data: RdsData) -> None:
        await self._rds_data.insert_one(rds_data.__dict__)

    @override
    async def find_rds_config_by_id(self, app_id: str) -> RdsConfig | None:
        data = await self._rds_config.find_one({"_id": app_id})
        return RdsConfig(**data) if data else None
