from typing import Any, override

from motor.motor_asyncio import AsyncIOMotorClient

from mercury.core.MongoClient import MongoClient
from mercury.core.Setting import Setting


class MotorClient(MongoClient):
    def __init__(self, setting: Setting):
        self.__client = AsyncIOMotorClient(setting.mongo)
        self.__db = self.__client[setting.project_name]
        self.__setting = setting

    @override
    async def find_one(self, table_name: str, query: dict[str, Any]) -> Any:
        """"""
        return await self.__db[table_name].find_one(query)

    @override
    async def close(self) -> None:
        self.__client.close()

    @property
    @override
    def client(self) -> AsyncIOMotorClient:
        """"""
        return self.__client

    @client.setter
    @override
    def client(self, client: AsyncIOMotorClient) -> None:
        """"""
        self.__client = client
        self.__db = self.__client[self.__setting.project_name]
