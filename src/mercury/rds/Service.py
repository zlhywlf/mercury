from datetime import date, datetime
from typing import Any, Callable, Coroutine

import httpx
import jmespath
import jsonschema
import orjson
from anyio import create_task_group
from jsonschema import validate

from mercury.app.utils import run_dynamic_method
from mercury.core.Context import Context
from mercury.rds.models.Content import Content
from mercury.rds.models.Task import Task
from mercury.rds.Plugin import Plugin


class Service:
    TASK_TABLE_NAME = "task"
    SENSITIVE_FIELD = ["userId", "userKey"]

    def __init__(self, param: dict[str, Any], ctx: Context, plugins: dict[str, type[Plugin]]):
        """"""
        self.__http_client = ctx.http_client
        self.__mongo_client = ctx.mongo_client
        self.__plugins = plugins
        self.__app_id: str | None = param.pop("appId", None)
        self.__param = param
        self.__rds_task: Task | None = None
        self.__content = Content(task_type="", param=self.__param, code=200, msg="", data=None)

    async def get_data(self) -> None:
        if not self.__app_id:
            self.__content.code = 404
            self.__content.msg = f"AppId({self.__app_id}) is None"
            return
        self.__rds_task = await self.find_task_by_id(self.__app_id)
        if not self.__rds_task:
            self.__content.code = 404
            self.__content.msg = f"AppId({self.__app_id}) does not exist"
            return
        t = self.__rds_task.type
        self.__content.task_type = t
        if t == "subject":
            self.__content.data = {}
            content = self.__content
        else:
            self.__content.data = []
            content = Content(
                task_type=self.__rds_task.type,
                param=self.__content.param or {},
                code=200,
                msg="",
                data=None,
            )
        await run_dynamic_method(self, f"handle_{t}", content, self.__content, self.__rds_task)
        if t == "subject" and isinstance(self.__content.data, dict):
            self.__content.data["createTime"] = datetime.now()
            self.__content.data["deadline"] = date.today()
            for k, v in self.__content.param.items():
                if k not in Service.SENSITIVE_FIELD:
                    self.__content.data[k] = v

    @property
    def app_id(self) -> str | None:
        """"""
        return self.__app_id

    async def handle_api(self, content: Content, parent: Content, rds_task: Task) -> None:
        """"""

        async def func() -> None:
            configs = {_.name: _.value for _ in (rds_task.configs or [])}
            path = configs.get("path")
            host = configs.get("host", "")
            url = f"{host}{path}"
            try:
                rp = await self.__http_client.request(url, configs.get("method", ""), content.param)
                content.data = rp.json()
            except (httpx.ConnectTimeout, httpx.ReadError) as e:
                content.code = 407
                arg = {_: content.param.get(_) for _ in rds_task.args} if rds_task.args else {}
                content.msg += f"{rds_task.name}_{path}_{arg}:请求错误{e}"

        await self.handle(content, parent, rds_task, func)

    async def handle_table(self, content: Content, parent: Content, rds_task: Task) -> None:
        """"""
        await self.handle_subject(content, parent, rds_task)

    async def handle_db(self, content: Content, parent: Content, rds_task: Task) -> None:
        """"""

    async def handle_subject(self, content: Content, parent: Content, rds_task: Task) -> None:
        """"""

        async def wrapper(*args: Any) -> None:
            await run_dynamic_method(self, args[0], args[1], args[2], args[3])

        async def func() -> None:
            content.data = {} if rds_task.type == "subject" else []

            if rds_task.tasks:
                async with create_task_group() as tg:
                    for task in rds_task.tasks:
                        sub_content = Content(
                            task_type=task.type,
                            param=content.param or {},
                            code=200,
                            msg="",
                            data=None,
                        )
                        tg.start_soon(wrapper, f"handle_{task.type}", sub_content, content, task)
            else:
                content.code = 201
                content.msg = "空白占位数据"

        await self.handle(content, parent, rds_task, func)

    @property
    def content(self) -> Content:
        """"""
        return self.__content

    async def handle(
        self,
        content: Content,
        parent: Content,
        rds_task: Task,
        func: Callable[[], Coroutine[Any, Any, None]],
    ) -> None:
        """"""
        plugins = []
        if rds_task.plugins:
            for meta in rds_task.plugins:
                if clazz := self.__plugins.get(meta.id):
                    plugins.append(clazz(meta, self))
                else:
                    raise RuntimeError(f"plugin {meta.id} not found")
        for plugin in plugins:
            await plugin.pre(content, parent, rds_task)

        if rds_task.args_schema:
            validate(instance=content.param, schema=orjson.loads(rds_task.args_schema))

        await func()

        for plugin in plugins:
            await plugin.post(content, parent, rds_task)

        if rds_task.data_schema:
            try:
                validate(
                    instance=content.model_dump(),
                    schema=orjson.loads(rds_task.data_schema),
                )
            except jsonschema.exceptions.ValidationError as e:
                content.code = 407
                arg = {_: content.param.get(_) for _ in rds_task.args} if rds_task.args else {}
                content.msg += f"{rds_task.name}:数据_{content.data}_{arg}_不符合预期_{e.message};"
            else:
                if not content.data:
                    content.code = 201

        async def wrapper(*args: Any) -> None:
            await run_dynamic_method(self, args[0], args[1], args[2], args[3])

        if rds_task.sub_tasks:
            async with create_task_group() as tg:
                for task in rds_task.sub_tasks:
                    params = []
                    if isinstance(content.data, dict):
                        params = [content.data]
                    if isinstance(content.data, list):
                        params = content.data
                    if task.configs:
                        for config in task.configs:
                            if config.name == "ParamFilter":
                                params = jmespath.search(config.value, params)
                    if params is None:
                        continue
                    for param in params:
                        sub_content = Content(
                            task_type=task.type,
                            param=param,
                            code=200,
                            msg="",
                            data=None,
                        )
                        tg.start_soon(wrapper, f"handle_{task.type}", sub_content, content, task)

        if parent is not content and parent.task_type == "subject" and isinstance(parent.data, dict):
            if rds_task.type == "subject":
                name = content.param.get("name") or rds_task.name
                if name in parent.data:
                    d = parent.data[name]
                    if isinstance(d, dict) and isinstance(content.data, dict):
                        parent.data[name] = d | content.data
                else:
                    parent.data[name] = content.data
            else:
                parent.data[rds_task.name] = content
            if content.code not in [201, 200] and parent.code == 200:
                parent.code = content.code
                parent.msg += content.msg
            return

        if parent.task_type != "subject" and rds_task.type == "subject":
            if isinstance(self.__content.data, dict):
                name = content.param.get("name") or rds_task.name
                if name in self.__content.data:
                    d = self.__content.data[name]
                    if isinstance(d, dict) and isinstance(content.data, dict):
                        self.__content.data[name] = d | content.data
                else:
                    self.__content.data[name or rds_task.name] = content.data
            return

        if isinstance(parent.data, list):
            if isinstance(content.data, list):
                parent.data.extend(content.data)
            elif isinstance(content.data, dict):
                parent.data.append(content.data)
            if content.code not in [201, 200] and parent.code == 200:
                parent.code = content.code
                parent.msg += content.msg

    async def find_task_by_id(self, app_id: str) -> Task | None:
        data = await self.__mongo_client.find_one(Service.TASK_TABLE_NAME, {"_id": app_id})
        return Task(**data) if data else None
