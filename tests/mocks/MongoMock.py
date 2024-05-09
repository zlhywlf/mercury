from typing import override

from mongomock_motor import AsyncMongoMockClient, AsyncMongoMockDatabase

from mercury.core.clients.Mongo import Mongo
from mercury.core.Setting import Setting


class MongoMock(Mongo[AsyncMongoMockDatabase]):
    def __init__(self, setting: Setting):
        super().__init__(setting)
        self.__client = AsyncMongoMockClient()

    @override
    async def get_db_by_name(self, name: str) -> AsyncMongoMockDatabase:
        """"""
        return self.__client[name]

    @override
    async def close(self) -> None:
        """"""
