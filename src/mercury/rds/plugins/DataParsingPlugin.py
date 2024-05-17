from typing import Any, override

import jmespath
import orjson
from jmespath import functions

from mercury.rds.models.Content import Content
from mercury.rds.models.PluginMeta import PluginMeta
from mercury.rds.models.Task import Task
from mercury.rds.Plugin import Plugin


class CustomFunctions(functions.Functions):
    @functions.signature({"types": ["string"]})
    def _func_to_json(self, field: str) -> Any:
        return orjson.loads(field)

    @functions.signature({"types": ["string", "number", "null"]}, {"types": ["string", "null"]})
    def _func_convert_unit(self, field: float | str | None, unit: str | None) -> float | None:
        if field is None:
            return field
        if isinstance(field, str) and not field:
            return None
        else:
            try:
                field = float(field)
            except ValueError:
                return None
        if unit in ["万元"]:
            field *= 10000
        return field

    @functions.signature({"types": ["string", "number"]}, {"types": ["object"]}, {"types": ["string"]})
    def _func_mapping(self, key: str | int, mapping: dict[str, Any], default: str) -> Any:
        """"""
        return mapping.get(str(key), default)


options = jmespath.Options(custom_functions=CustomFunctions())


class DataParsingPlugin(Plugin):
    def __init__(self, meta: PluginMeta, service: object) -> None:
        super().__init__(meta, service)
        self.__expression = self.config.get("expression")

    @override
    async def post(self, current: Content, parent: Content, rds_task: Task) -> None:
        """"""
        if self.__expression and current.data:
            current.data = jmespath.search(self.__expression, current.data, options=options)
            if current.data is None:
                raise RuntimeError(f"{rds_task.name}Data parsing failed")

    @classmethod
    @override
    def plugin_id(cls) -> str:
        """"""
        return "data_parsing"
