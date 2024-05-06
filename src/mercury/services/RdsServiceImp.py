from typing import Any, Callable, override

from anyio import create_task_group
from jsonschema import validate

from mercury.core.mappers.RdsMapper import RdsMapper
from mercury.core.services.RdsService import RdsService
from mercury.models.AppContext import AppContext
from mercury.models.rds.Content import Content
from mercury.models.rds.Task import Task
from mercury.utils.ModuleUtil import run_dynamic_method


class RdsServiceImp(RdsService):

    def __init__(self, mapper: RdsMapper, params: dict, ctx: AppContext):
        """"""
        self.__mapper = mapper
        self.__app_id = params.pop('appId', None)
        self.__params = params
        self.__rds_task: Task | None = None
        self.__http_client = ctx.http_client
        self.__mongo_client = ctx.mongo_client
        self.__plugins = ctx.rds_plugins
        self.__content = Content(type="", params=[self.__params], code=200, msg="", data=None, sub_params=None)

    @override
    async def get_data(self) -> Any:
        t = self.__rds_task.type
        self.__content.type = t
        if t == "subject":
            self.__content.data = {**self.__params}
        else:
            self.__content.data = []
        self.__content.sub_params = self.__content.params
        return await run_dynamic_method(self, f"handle_{t}", self.__content, self.__rds_task)

    @override
    async def get_rds_task(self) -> bool:
        """"""
        if not self.__app_id:
            return False
        self.__rds_task = await self.__mapper.find_rds_task_by_id(self.__app_id)
        return self.__rds_task is not None

    @property
    @override
    def app_id(self) -> str | None:
        """"""
        return self.__app_id

    @override
    async def handle_api(self, parent: Content, rds_task: Task) -> None:
        """"""

        async def func(content: Content) -> list:
            data = []
            for param in content.params:
                validate(instance=param, schema=rds_task.args_schema)
                configs = {_.name: _.value for _ in rds_task.configs}
                rp = await self.__http_client.request(configs.get("url"), configs.get("method"), param)
                data.append(rp)
            return data

        await self.handle(parent, rds_task, func)

    @override
    async def handle_table(self, parent: Content, rds_task: Task) -> None:
        """"""

        async def func(content: Content) -> list:

            data = []
            content.sub_params = content.params

            async def wrapper(*args) -> None:
                d = await run_dynamic_method(self, args[0], args[1], args[2])
                data.append(d)

            if rds_task.sub_tasks:
                async with create_task_group() as tg:
                    for sub_task in rds_task.sub_tasks:
                        tg.start_soon(wrapper, f"handle_{sub_task.type}", content, sub_task)

            return data

        await self.handle(parent, rds_task, func)

    @override
    async def handle_db(self, parent: Content, rds_task: Task) -> None:
        """"""
        # validate(instance=params, schema=rds_task.args_schema)

    @override
    async def handle_subject(self, parent: Content, rds_task: Task) -> None:
        """"""

    @property
    @override
    def content(self) -> Content:
        """"""
        return self.__content

    async def handle(self, parent: Content, rds_task: Task, func: Callable) -> None:
        """"""
        content = Content(type=rds_task.type, params=parent.sub_params, code=200, msg="", data=[], sub_params=None)
        plugins = []
        if rds_task.plugins:
            for meta in rds_task.plugins:
                if clazz := self.__plugins.get(meta.id):
                    plugins.append(clazz(meta, self.__http_client, self.__mongo_client))
                else:
                    raise RuntimeError(f"plugin {meta.id} not found")
        for plugin in plugins:
            plugin.pre(content, parent)

        for param in content.params:
            validate(instance=param, schema=rds_task.args_schema)

        data = await func(content)

        content.data.extend(data)
        for plugin in plugins:
            plugin.post(content, parent)

        if rds_task.type == "subject" and self.__content:
            assert isinstance(self.__content.data, dict)
            self.__content.data[rds_task.name] = content
            return
        if parent.type == "subject":
            assert isinstance(parent.data, dict)
            parent.data[rds_task.name] = content
            return
        assert isinstance(parent.data, list)
        parent.data.extend(content.data)
