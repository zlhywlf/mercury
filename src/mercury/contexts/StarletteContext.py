from typing import Self, override

from mercury.core.Application import Application
from mercury.core.clients.Http import Http
from mercury.core.clients.Mongo import Mongo
from mercury.core.Context import Context
from mercury.core.Plugin import Plugin


class StarletteContext(Context[Application]):

    def __init__(self, *, http_client: Http, mongo_client: Mongo,
                 rds_plugins: dict[str, type[Plugin]]):
        super().__init__(http_client=http_client, mongo_client=mongo_client, rds_plugins=rds_plugins)
        self.__application: Application | None = None
        self.__http_client = http_client
        self.__mongo_client = mongo_client
        self.__rds_plugins = rds_plugins

    @override
    async def __aenter__(self) -> dict[str, Self]:
        return {"ctx": self}

    @override
    async def __aexit__(self, *exc_info: object) -> None:
        await self.__http_client.close()
        await self.__mongo_client.close()

    @override
    def __call__(self, application: Application) -> Self:
        self.__application = application
        return self

    @property
    @override
    def application(self) -> Application:
        """"""
        return self.__application

    @property
    @override
    def http_client(self) -> Http:
        """"""
        return self.__http_client

    @property
    @override
    def mongo_client(self) -> Mongo:
        """"""
        return self.__mongo_client

    @property
    @override
    def rds_plugins(self) -> dict[str, type[Plugin]]:
        """"""
        return self.__rds_plugins
