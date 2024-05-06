from typing import override

import orjson
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from mercury.mappers.AsyncRdsMapperImp import AsyncRdsMapperImp
from mercury.models.AppContext import AppContext
from mercury.services.RdsServiceImp import RdsServiceImp
from mercury.utils.EncryptionUtil import encrypt_by_md5


class RdsMiddleware(BaseHTTPMiddleware):
    """"""

    @override
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        ctx = request.state.ctx
        assert isinstance(ctx, AppContext)
        mapper = AsyncRdsMapperImp(ctx.mongo_client.get_db_by_name(ctx.application.setting.project_name),
                                   ctx.application.setting)
        rds_key = ctx.application.setting.rds_key
        body = await request.body()
        json_params = orjson.loads(body) if body else {}
        params = {**request.path_params, **request.query_params, **json_params}
        if encrypt_by_md5(f"{params.get('userId')}+", rds_key) != params.get('userKey'):
            return JSONResponse({"msg": "Authentication failed"}, status_code=400)
        request.state.service = RdsServiceImp(mapper, params, ctx.http_client)
        return await call_next(request)
