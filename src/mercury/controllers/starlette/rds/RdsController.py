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
        assert isinstance(service, AsyncRdsService)
        ok = await service.get_rds_task()
        if not ok:
            return JSONResponse({"msg": f"AppId({service.app_id}) does not exist"}, status_code=400)
        ret = await service.get_data()
        return JSONResponse({'data': ret})

    async def post(self, request: Request):
        return await self.get(request)
