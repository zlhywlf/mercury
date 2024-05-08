from typing import Any, override

from httpx import AsyncClient

from mercury.core.clients.Http import Http
from mercury.core.Setting import Setting
from mercury.utils.ModuleUtil import run_dynamic_method


class HttpHttpx(Http[AsyncClient]):

    def __init__(self, setting: Setting):
        super().__init__(setting)
        self.__client = AsyncClient()

    @override
    async def request(self, url: str, method: str, params: dict) -> Any:
        return await run_dynamic_method(self, method.lower(), url, params)

    @override
    async def get(self, url: str, params: dict) -> Any:
        rp = await self.__client.get(url, params=params)
        return rp.json()

    @override
    async def post(self, url: str, params: dict) -> Any:
        """"""
        rp = await self.__client.post(url, json=params)
        return rp.json()

    @override
    async def close(self) -> None:
        """"""
        await self.__client.aclose()

    @property
    @override
    def client(self) -> AsyncClient:
        """"""
        return self.__client

    @client.setter
    @override
    def client(self, client: AsyncClient) -> None:
        """"""
        self.__client = client
