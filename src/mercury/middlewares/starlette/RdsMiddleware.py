from typing import override

import orjson
from motor.motor_asyncio import AsyncIOMotorDatabase
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.types import ASGIApp

from mercury.core.Application import Application
from mercury.mappers.AsyncRdsMapperImp import AsyncRdsMapperImp
from mercury.services.AsyncRdsServiceImp import AsyncRdsServiceImp
from mercury.utils.EncryptionUtil import encrypt_by_md5


class RdsMiddleware(BaseHTTPMiddleware):
    """"""

    def __init__(self, app: ASGIApp, application: Application, async_db: AsyncIOMotorDatabase) -> None:
        super().__init__(app)
        self.__rds_key = application.setting.rds_key
        self.__mapper = AsyncRdsMapperImp(async_db, application.setting)

    @override
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        path_params = request.path_params
        query_params = request.query_params
        body = await request.body()
        json_params = orjson.loads(body) if body else {}
        params = {**path_params, **query_params, **json_params}
        if encrypt_by_md5(f"{params.get('userId')}+", self.__rds_key) != params.get('userKey'):
            return JSONResponse({"msg": "Authentication failed"}, status_code=400)
        request.state.service = AsyncRdsServiceImp(self.__mapper, params, request.state.http_client)
        return await call_next(request)
