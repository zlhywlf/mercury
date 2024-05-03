from typing import override

from mercury.core.mappers.AsyncRdsMapper import AsyncRdsMapper
from mercury.core.services.AsyncRdsService import AsyncRdsService
from mercury.models.rds.Task import Task


class AsyncRdsServiceImp(AsyncRdsService):

    def __init__(self, mapper: AsyncRdsMapper):
        """"""
        self.__mapper = mapper

    @override
    def get_data(self):
        pass

    @override
    async def get_rds_task(self, app_id: str) -> Task | None:
        """"""
        await self.__mapper.find_rds_task_by_id(app_id)
        return await self.__mapper.find_rds_task_by_id(app_id)
