from typing import override

import jmespath

from mercury.rds.models.Content import Content
from mercury.rds.models.PluginMeta import PluginMeta
from mercury.rds.models.Task import Task
from mercury.rds.Plugin import Plugin
from mercury.rds.plugins.DataParsingPlugin import options


class CustomDataPlugin(Plugin):
    def __init__(self, meta: PluginMeta, service: object) -> None:
        super().__init__(meta, service)

    @override
    async def post(self, current: Content, parent: Content, rds_task: Task) -> None:
        """"""
        if isinstance(parent.data, dict) and isinstance(current.data, dict):
            for key, exp in self.config.items():
                path = exp.split(".")
                if not path:
                    continue
                k = path.pop(0)
                tbl = current.data.get(k)
                if isinstance(tbl, Content):
                    tbl = tbl.model_dump()
                    current.data[k] = tbl
                parent.data[key] = jmespath.search(".".join(path), tbl, options=options)

    @classmethod
    @override
    def plugin_id(cls) -> str:
        """"""
        return "custom_data"
