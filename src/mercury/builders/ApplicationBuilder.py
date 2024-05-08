from typing import Self

from mercury.core.Application import Application
from mercury.core.clients.Http import Http
from mercury.core.clients.Mongo import Mongo
from mercury.core.Context import Context
from mercury.core.Controller import Controller
from mercury.core.Plugin import Plugin
from mercury.core.Setting import Setting
from mercury.utils.ModuleUtil import find_class_by_type, get_modules


class ApplicationBuilder:

    def __init__(self, app_cls: type[Application], context: type[Context]) -> None:
        self.__app_cls = app_cls
        self.__context_cls: type[Context] = context
        self.__setting: Setting | None = None
        self.__controllers: list[type[Controller]] = []
        self.__rds_plugins: dict[str, type[Plugin]] = {}
        self.__http_client: Http | None = None
        self.__mongo_client: Mongo | None = None

    def add_setting(self, setting: Setting) -> Self:
        self.__setting = setting
        return self

    def add_http_client(self, http_client: Http) -> Self:
        self.__http_client = http_client
        return self

    def add_mongo_client(self, mongo_client: Mongo) -> Self:
        self.__mongo_client = mongo_client
        return self

    def add_rds_plugins(self, pkg: str) -> Self:
        for m in get_modules(pkg):
            if clazz := find_class_by_type(m, Plugin):
                self.__rds_plugins[clazz.plugin_id()] = clazz
        return self

    def add_controllers(self, *controllers: type[Controller]) -> Self:
        self.__controllers.extend(controllers)
        return self

    def build(self) -> Application:
        if not self.__setting:
            raise RuntimeError(f'Application {self.__app_cls} has no setting')
        if not self.__http_client:
            raise RuntimeError(f'Application {self.__app_cls} has no http_client')
        if not self.__mongo_client:
            raise RuntimeError(f'Application {self.__app_cls} has no mongo_client')
        ctx = self.__context_cls(http_client=self.__http_client, mongo_client=self.__mongo_client,
                                 rds_plugins=self.__rds_plugins)
        return self.__app_cls(lifespan=ctx, setting=self.__setting, controllers=self.__controllers)
