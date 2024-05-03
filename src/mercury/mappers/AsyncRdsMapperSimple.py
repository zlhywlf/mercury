from typing import override

from motor.motor_asyncio import AsyncIOMotorDatabase

from mercury.core.mappers.AsyncRdsMapper import AsyncRdsMapper
from mercury.models.rds.Task import Task
from mercury.models.rds.Data import Data
from mercury.core.Setting import Setting


class AsyncRdsMapperSimple(AsyncRdsMapper):
    """"""

    def __init__(self, db: AsyncIOMotorDatabase, setting: Setting):
        self._rds_data = db[setting.rds_data_table_name]
        self._rds_config = db[setting.rds_task_table_name]

    @override
    async def insert_rds_data(self, rds_data: Data) -> None:
        await self._rds_data.insert_one(rds_data.__dict__)

    @override
    async def find_rds_config_by_id(self, app_id: str) -> Task | None:
        data = await self._rds_config.find_one({"_id": app_id})
        return Task(**data) if data else None
