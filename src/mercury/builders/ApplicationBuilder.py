from typing import Self

from mercury.core.Application import Application
from mercury.core.Controller import Controller
from mercury.core.Plugin import Plugin
from mercury.core.Setting import Setting
from mercury.utils.ModuleUtil import find_class_by_type, get_modules


class ApplicationBuilder:

    def __init__(self, app_cls: type[Application]) -> None:
        self.__app_cls = app_cls
        self.__setting: Setting | None = None
        self.__controllers: list[type[Controller]] = []
        self.__rds_plugins: dict[str, type[Plugin]] = {}

    def add_setting(self, setting: Setting) -> Self:
        self.__setting = setting
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
        return self.__app_cls(setting=self.__setting, controllers=self.__controllers, rds_plugins=self.__rds_plugins)
