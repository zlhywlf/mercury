from typing import override

from motor.motor_asyncio import AsyncIOMotorClient

from mercury.core.clients.Mongo import Mongo


class MongoMotor(Mongo):

    def __init__(self, client: AsyncIOMotorClient):
        super().__init__()
        self.__client = client

    @override
    def get_db_by_name(self, name: str):
        return self.__client[name]
