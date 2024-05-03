from typing import override

from motor.motor_asyncio import AsyncIOMotorDatabase

from mercury.core.mappers.AsyncRdsMapper import AsyncRdsMapper
from mercury.core.Setting import Setting
from mercury.models.rds.Data import Data
from mercury.models.rds.Task import Task


class AsyncRdsMapperImp(AsyncRdsMapper):
    """"""

    def __init__(self, db: AsyncIOMotorDatabase, setting: Setting):
        self.__rds_data = db[setting.rds_data_table_name]
        self.__rds_config = db[setting.rds_task_table_name]

    @override
    async def insert_rds_data(self, rds_data: Data) -> None:
        await self.__rds_data.insert_one(rds_data.__dict__)

    @override
    async def find_rds_task_by_id(self, app_id: str) -> Task | None:
        data = await self.__rds_config.find_one({"_id": app_id})
        return Task(**data) if data else None
