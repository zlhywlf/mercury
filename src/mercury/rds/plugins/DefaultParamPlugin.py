from typing import override

from mercury.rds.models.Content import Content
from mercury.rds.models.PluginMeta import PluginMeta
from mercury.rds.models.Task import Task
from mercury.rds.Plugin import Plugin


class DefaultParamPlugin(Plugin):
    def __init__(self, meta: PluginMeta, service: object) -> None:
        super().__init__(meta, service)

    @override
    async def pre(self, current: Content, parent: Content, rds_task: Task) -> None:
        """"""
        if current.param:
            for k, v in self.config.items():
                if k not in current.param:
                    current.param[k] = v

    @classmethod
    @override
    def plugin_id(cls) -> str:
        """"""
        return "default_param"
