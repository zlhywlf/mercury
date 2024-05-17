import math
from datetime import datetime
from typing import Any, override

import jmespath
from anyio import create_task_group

from mercury.app.utils import run_dynamic_method
from mercury.rds.models.Content import Content
from mercury.rds.models.PluginMeta import PluginMeta
from mercury.rds.models.Task import Task
from mercury.rds.Plugin import Plugin


class DynamicApiPlugin(Plugin):
    def __init__(self, meta: PluginMeta, service: object):
        super().__init__(meta, service)
        self.__total = self.config.get("total_expression")
        self.__size = self.config.get("size_expression")

    @override
    async def post(self, current: Content, parent: Content, rds_task: Task) -> None:
        """"""

        async def wrapper(*args: Any) -> None:
            await run_dynamic_method(self.service, args[0], args[1], args[2], args[3])

        if rds_task.type == "api" and current.data and self.__total and self.__size:
            total = jmespath.search(self.__total, current.data)
            size = jmespath.search(self.__size, current.data)
            if total and size:
                if total <= size:
                    return
                counts = math.ceil(total / size)
                async with create_task_group() as tg:
                    for num in range(2, counts + 1):
                        task = Task(
                            _id=rds_task.key,
                            name=f"{rds_task.name}_{num}",
                            type=rds_task.type,
                            plugins=(
                                [_ for _ in rds_task.plugins if _.id != DynamicApiPlugin.plugin_id()]
                                if rds_task.plugins
                                else None
                            ),
                            args=rds_task.args,
                            args_schema=rds_task.args_schema,
                            data_schema=rds_task.data_schema,
                            configs=rds_task.configs,
                            tasks=None,
                            sub_tasks=None,
                            description=rds_task.description,
                            create_time=datetime.now(),
                            update_time=datetime.now(),
                        )
                        param = current.param | {"page_number": num, "page_size": size}
                        content = Content(
                            task_type=rds_task.type,
                            param=param,
                            code=200,
                            msg="",
                            data=None,
                        )
                        tg.start_soon(wrapper, f"handle_{rds_task.type}", content, parent, task)

    @classmethod
    @override
    def plugin_id(cls) -> str:
        """"""
        return "dynamic_api"
