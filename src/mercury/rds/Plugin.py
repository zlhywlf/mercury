from abc import ABC, abstractmethod
from typing import Any

from mercury.rds.models.Content import Content
from mercury.rds.models.PluginMeta import PluginMeta
from mercury.rds.models.Task import Task


class Plugin(ABC):
    def __init__(self, meta: PluginMeta, service: object):
        self.__config = {_.name: _.value for _ in meta.configs}
        self.__service = service

    async def pre(self, current: Content, parent: Content, rds_task: Task) -> None:
        """"""
        return

    async def post(self, current: Content, parent: Content, rds_task: Task) -> None:
        """"""
        return

    @property
    def config(self) -> dict[str, Any]:
        """"""
        return self.__config

    @property
    def service(self) -> object:
        """"""
        return self.__service

    @classmethod
    @abstractmethod
    def plugin_id(cls) -> str:
        """"""
