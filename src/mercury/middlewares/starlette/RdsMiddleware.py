from typing import override

import orjson
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.types import ASGIApp

from mercury.core.Application import Application
from mercury.utils.EncryptionUtil import encrypt_by_md5


class RdsMiddleware(BaseHTTPMiddleware):
    """"""

    def __init__(self, app: ASGIApp, application: Application) -> None:
        super().__init__(app)
        self._rds_config = application.rds_config
        self._rds_key = application.setting.rds_key

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
        if not app_id or app_id not in self._rds_config:
            return JSONResponse({"msg": f"appId: {app_id} not exist"}, status_code=400)
        request.state.app_config = self._rds_config[app_id]
        request.state.params = params
        return await call_next(request)
