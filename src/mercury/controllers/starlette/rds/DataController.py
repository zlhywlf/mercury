from typing import override

from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse

from mercury.core.Controller import Controller


class DataController(Controller, HTTPEndpoint):

    @classmethod
    @override
    def path(cls) -> list[str]:
        return ["/rds/data", "/rds/data/{appId}"]

    async def get(self, request: Request):
        app_config = request.state.app_config
        params = request.state.params
        return JSONResponse({'data': app_config})

    async def post(self, request: Request):
        return await self.get(request)
