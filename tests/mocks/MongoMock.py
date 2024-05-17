from typing import Any, override

from mercury.core.MongoClient import MongoClient
from mercury.core.Setting import Setting
from mongomock_motor import AsyncMongoMockClient


class MongoMock(MongoClient):
    def __init__(self, setting: Setting):
        self.__client = AsyncMongoMockClient()
        self.__db = self.__client[setting.project_name]

    @override
    async def find_one(self, table_name: str, query: dict) -> Any:
        """"""
        return await self.__db[table_name].find_one(query)

    @override
    async def close(self) -> None:
        """"""

    @property
    @override
    def client(self) -> AsyncMongoMockClient:
        """"""
        return self.__client

    @client.setter
    @override
    def client(self, client: AsyncMongoMockClient) -> None:
        """"""
