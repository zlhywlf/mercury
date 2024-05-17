from typing import Any, override

from httpx import AsyncClient, Response, Timeout

from mercury.app.utils import run_dynamic_method
from mercury.core.HttpClient import HttpClient
from mercury.core.Setting import Setting


class HttpxClient(HttpClient[AsyncClient, Response]):  # type: ignore[type-arg]
    def __init__(self, setting: Setting):
        self.__client = AsyncClient(timeout=Timeout(300))

    @override
    async def request(self, url: str, method: str, params: dict[str, Any]) -> Response:
        response = await run_dynamic_method(self, method.lower(), url, params)
        assert isinstance(response, Response)
        return response

    @override
    async def get(self, url: str, params: dict[str, Any]) -> Response:
        return await self.__client.get(url, params=params)

    @override
    async def post(self, url: str, params: dict[str, Any]) -> Response:
        return await self.__client.post(url, json=params)

    @override
    async def close(self) -> None:
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
