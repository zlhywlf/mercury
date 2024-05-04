from typing import Any, override

from httpx import AsyncClient

from mercury.core.clients.Http import Http
from mercury.utils.ModuleUtil import run_dynamic_method


class HttpHttpx(Http):

    def __init__(self, *, client: AsyncClient):
        super().__init__()
        self.__client = client

    @override
    async def request(self, url: str, method: str, params: dict) -> Any:
        return await run_dynamic_method(self, method.lower(), url, params)

    @override
    async def get(self, url: str, params: dict) -> Any:
        rp = await self.__client.get(url, params=params)
        return rp.json()
