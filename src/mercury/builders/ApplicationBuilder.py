from typing import Self

from mercury.core.Application import Application
from mercury.core.Controller import Controller
from mercury.core.Setting import Setting


class ApplicationBuilder:

    def __init__(self, app_cls: type[Application]) -> None:
        self.__app_cls = app_cls
        self.__setting: Setting | None = None
        self.__controllers: list[type[Controller]] = []

    def add_setting(self, setting: Setting) -> Self:
        self.__setting = setting
        return self

    def add_controllers(self, *controllers: type[Controller]) -> Self:
        self.__controllers.extend(controllers)
        return self

    def build(self) -> Application:
        if not self.__setting:
            raise RuntimeError(f'Application {self.__app_cls} has no setting')
        return self.__app_cls(setting=self.__setting, controllers=self.__controllers)
