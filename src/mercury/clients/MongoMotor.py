from typing import override

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from mercury.core.clients.Mongo import Mongo
from mercury.core.Setting import Setting


class MongoMotor(Mongo[AsyncIOMotorDatabase]):

    def __init__(self, setting: Setting):
        super().__init__(setting)
        self.__client = AsyncIOMotorClient(setting.mongo)

    @override
    async def get_db_by_name(self, name: str) -> AsyncIOMotorDatabase:
        return self.__client[name]

    @override
    async def close(self) -> None:
        """"""
        self.__client.close()
