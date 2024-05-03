from typing import override

from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse

from mercury.core.Controller import Controller
from mercury.core.services.AsyncRdsService import AsyncRdsService
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
        service = request.state.service
        params = request.state.params
        assert isinstance(service, AsyncRdsService)
        app_id = params.get("appId")
        rds_task = await service.get_rds_task(app_id)
        if not rds_task:
            return JSONResponse({"msg": f"AppId({app_id}) does not exist"}, status_code=400)
        service.get_data()
        return JSONResponse({'params': 'params'})

    async def post(self, request: Request):
        return await self.get(request)
