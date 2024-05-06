from typing import override

from mercury.core.clients.Http import Http
from mercury.core.clients.Mongo import Mongo
from mercury.core.Plugin import Plugin
from mercury.models.rds.Content import Content
from mercury.models.rds.PluginMeta import PluginMeta


class ParamMapPlugin(Plugin):
    def __init__(self, meta: PluginMeta, http_client: Http, mongo_client: Mongo):
        super().__init__(meta, http_client, mongo_client)
        self.__map = {_.name: _.value for _ in meta.configs}

    @override
    def pre(self, current: Content, parent: Content) -> None:
        """"""
        params = []
        for _ in parent.sub_params:
            param = {}
            for k, v in self.__map.items():
                if k not in _:
                    continue
                param[v] = _[k]
            params.append(param)
        current.params = params

    @classmethod
    @override
    def plugin_id(cls) -> str:
        """"""
        return "param_map"
