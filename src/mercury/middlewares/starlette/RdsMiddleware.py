from typing import override

import orjson
from motor.motor_asyncio import AsyncIOMotorDatabase
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.types import ASGIApp

from mercury.core.Application import Application
from mercury.mappers.AsyncRdsMapperSimple import AsyncRdsMapperSimple
from mercury.utils.EncryptionUtil import encrypt_by_md5


class RdsMiddleware(BaseHTTPMiddleware):
    """"""

    def __init__(self, app: ASGIApp, application: Application, async_db: AsyncIOMotorDatabase) -> None:
        super().__init__(app)
        self._rds_config = application.rds_config
        self._rds_key = application.setting.rds_key
        self._mapper = AsyncRdsMapperSimple(async_db)

    @override
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        path_params = request.path_params
        query_params = request.query_params
        body = await request.body()
        json_params = orjson.loads(body) if body else {}
        params = {**path_params, **query_params, **json_params}
        if encrypt_by_md5(f"{params.get('userId')}+", self._rds_key) != params.get('userKey'):
            return JSONResponse({"msg": "认证失败"}, status_code=400)
        app_id = params.get("appId")
        rds_config = await self._mapper.find_rds_config_by_id(app_id)
        if not rds_config:
            return JSONResponse({"msg": f"appId: {app_id} not exist"}, status_code=400)
        request.state.rds_config = rds_config
        request.state.params = params
        request.state.mapper = self._mapper
        return await call_next(request)
