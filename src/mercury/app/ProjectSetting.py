from typing import override

from starlette.config import Config

from mercury.core.Setting import Setting


class ProjectSetting(Setting):
    def __init__(self) -> None:
        self.__config = Config()
        self.__debug = self.__config("DEBUG", cast=bool, default=False)
        self.__project_name = self.__config("PROJECT_NAME", cast=str, default="mercury")
        self.__app_key = self.__config("RDS_KEY", cast=str, default="key")
        self.__mongo = self.__config("MONGO", cast=str, default="mongodb://localhost:27017")

    @property
    @override
    def debug(self) -> bool:
        """"""
        return self.__debug

    @property
    @override
    def project_name(self) -> str:
        """"""
        return self.__project_name

    @property
    @override
    def app_key(self) -> str:
        """"""
        return self.__app_key

    @property
    @override
    def mongo(self) -> str:
        """"""
        return self.__mongo
