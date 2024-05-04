from typing import Any, override

from httpx import AsyncClient

from mercury.core.clients.Http import Http


class HttpHttpx(Http):

    def __init__(self, *, client: AsyncClient):
        super().__init__()
        self.__client = client

    @override
    async def request(self, url: str, method: str, params: dict)-> Any:
        handler = getattr(self, method.lower())
        if not handler:
            raise RuntimeError(f'Method {method} not supported')
        return await handler(url, params)

    @override
    async def get(self, url: str, params: dict)-> Any:
        rp = await self.__client.get(url, params=params)
        return rp.json()
