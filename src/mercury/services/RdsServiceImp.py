from typing import Any, override

from anyio import create_task_group
from jsonschema import validate

from mercury.core.clients.Http import Http
from mercury.core.mappers.RdsMapper import RdsMapper
from mercury.core.services.RdsService import RdsService
from mercury.models.rds.Task import Task
from mercury.utils.ModuleUtil import run_dynamic_method


class RdsServiceImp(RdsService):

    def __init__(self, mapper: RdsMapper, params: dict, http_client: Http):
        """"""
        self.__mapper = mapper
        self.__app_id = params.pop('appId', None)
        self.__params = params
        self.__rds_task: Task | None = None
        self.__http_client = http_client

    @override
    async def get_data(self) -> Any:
        t = self.__rds_task.type
        return await run_dynamic_method(self, f"handle_{t}", self.__params, self.__rds_task)

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
    async def handle_api(self, params: dict, rds_task: Task) -> Any:
        """"""
        validate(instance=params, schema=rds_task.args_schema)
        args = {_: params[_] for _ in rds_task.args}
        configs = {_.name: _.value for _ in rds_task.configs}
        rp = await self.__http_client.request(configs.get("url"), configs.get("method"), args)
        return rp

    @override
    async def handle_app(self, params: dict, rds_task: Task) -> Any:
        """"""
        validate(instance=params, schema=rds_task.args_schema)

        data = []

        async def wrapper(*args) -> None:
            d = await run_dynamic_method(self, args[0], args[1], args[2])
            data.append(d)

        if rds_task.sub_tasks:
            async with create_task_group() as tg:
                for sub_task in rds_task.sub_tasks:
                    tg.start_soon(wrapper, f"handle_{sub_task.type}", params, sub_task)
        return data

    @override
    async def handle_db(self, params: dict, rds_task: Task) -> Any:
        """"""
        validate(instance=params, schema=rds_task.args_schema)
