from typing import Self, override

from starlette.applications import Starlette

from mercury.core.Context import Context
from mercury.core.HttpClient import HttpClient
from mercury.core.MongoClient import MongoClient
from mercury.core.Setting import Setting


class StarletteContext(Context[Starlette]):  # type: ignore[type-arg]
    def __init__(self, *, setting: Setting, http_client: HttpClient, mongo_client: MongoClient):
        self.__application: Starlette | None = None
        self.__http_client = http_client
        self.__mongo_client = mongo_client
        self.__setting = setting

    @override
    async def __aenter__(self) -> dict[str, Self]:
        return {"ctx": self}

    @override
    async def __aexit__(self, *exc_info: object) -> None:
        await self.__http_client.close()
        await self.__mongo_client.close()

    @override
    def __call__(self, application: Starlette) -> Self:
        self.__application = application
        return self

    @property
    @override
    def application(self) -> Starlette | None:
        return self.__application

    @property
    @override
    def http_client(self) -> HttpClient:
        return self.__http_client

    @property
    @override
    def mongo_client(self) -> MongoClient:
        return self.__mongo_client

    @mongo_client.setter
    @override
    def mongo_client(self, mongo_client: MongoClient) -> None:
        """"""
        self.__mongo_client = mongo_client

    @property
    @override
    def setting(self) -> Setting:
        return self.__setting
