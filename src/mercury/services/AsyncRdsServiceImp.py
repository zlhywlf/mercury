from typing import Any, override

from jsonschema import validate

from mercury.core.clients.Http import Http
from mercury.core.mappers.AsyncRdsMapper import AsyncRdsMapper
from mercury.core.services.AsyncRdsService import AsyncRdsService
from mercury.models.rds.Task import Task


class AsyncRdsServiceImp(AsyncRdsService):

    def __init__(self, mapper: AsyncRdsMapper, params: dict, http_client: Http):
        """"""
        self.__mapper = mapper
        self.__app_id = params.pop('appId', None)
        self.__params = params
        self.__rds_task: Task | None = None
        self.__http_client = http_client

    @override
    async def get_data(self) -> Any:
        t = self.__rds_task.type
        handler = getattr(self, f"handle_{t}")
        if not handler:
            raise RuntimeError(f'Task {t} not supported')
        return await handler()

    @override
    async def get_rds_task(self) -> bool:
        """"""
        if not self.__app_id:
            return False
        self.__rds_task = await self.__mapper.find_rds_task_by_id(self.__app_id)
        validate(instance=self.__params, schema=self.__rds_task.args_schema)
        return self.__rds_task is not None

    @property
    @override
    def app_id(self) -> str | None:
        """"""
        return self.__app_id

    @override
    async def handle_api(self) -> Any:
        """"""
        args = {_: self.__params[_] for _ in self.__rds_task.args}
        configs = {_["name"]: _["value"] for _ in self.__rds_task.configs}
        rp = await self.__http_client.request(configs.get("url"), configs.get("method"), args)
        return rp

    @override
    async def handle_app(self) -> Any:
        """"""

    @override
    async def handle_db(self) -> Any:
        """"""
