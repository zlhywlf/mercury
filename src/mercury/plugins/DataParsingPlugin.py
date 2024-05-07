from typing import override

import jmespath

from mercury.core.clients.Http import Http
from mercury.core.clients.Mongo import Mongo
from mercury.core.Plugin import Plugin
from mercury.models.rds.Content import Content
from mercury.models.rds.PluginMeta import PluginMeta
from mercury.models.rds.Task import Task


class DataParsingPlugin(Plugin):
    def __init__(self, meta: PluginMeta, http_client: Http, mongo_client: Mongo):
        super().__init__(meta, http_client, mongo_client)
        self.__expression = None
        for config in meta.configs:
            if config.name == "expression":
                self.__expression = config.value
                break

    @override
    def post(self, current: Content, parent: Content, rds_task: Task) -> None:
        """"""
        if self.__expression and current.data:
            current.data = jmespath.search(self.__expression, current.data)
            if not current.data:
                raise RuntimeError(f"{rds_task.name}Data parsing failed")

    @classmethod
    @override
    def plugin_id(cls) -> str:
        """"""
        return "data_parsing"
