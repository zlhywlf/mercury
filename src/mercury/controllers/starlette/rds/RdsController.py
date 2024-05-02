from typing import override

from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse

from mercury.core.Controller import Controller
from mercury.middlewares.starlette.RdsMiddleware import RdsMiddleware


class RdsController(Controller, HTTPEndpoint):

    @classmethod
    @override
    def paths(cls) -> list[str]:
        return ["/rds", "/rds/{appId}"]

    @classmethod
    @override
    def middlewares(cls) -> list[type[RdsMiddleware]]:
        return [RdsMiddleware]

    async def get(self, request: Request):
        rds_config = request.state.rds_config
        params = request.state.params
        return JSONResponse({'params': params})

    async def post(self, request: Request):
        return await self.get(request)
