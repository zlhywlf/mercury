from typing import override

import orjson
from starlette.middleware.base import (
    BaseHTTPMiddleware,
    DispatchFunction,
    RequestResponseEndpoint,
)
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.types import ASGIApp

import mercury.rds.plugins
from mercury.app.utils import encrypt_by_md5, find_class_by_type, get_modules
from mercury.core.Context import Context
from mercury.rds.Plugin import Plugin
from mercury.rds.Service import Service


class Middleware(BaseHTTPMiddleware):
    """"""

    def __init__(self, app: ASGIApp, dispatch: DispatchFunction | None = None) -> None:
        super().__init__(app, dispatch)
        self.__rds_plugins = {}
        for m in get_modules(mercury.rds.plugins.__name__):
            if clazz := find_class_by_type(m, Plugin):
                self.__rds_plugins[clazz.plugin_id()] = clazz

    @override
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        ctx: Context = request.state.ctx
        rds_key = ctx.setting.app_key
        body = await request.body()
        json_params = orjson.loads(body) if body else {}
        params = {**request.path_params, **request.query_params, **json_params}
        if encrypt_by_md5(f"{params.get('userId')}+", rds_key) != params.get("userKey"):
            return JSONResponse({"msg": "Authentication failed"}, status_code=400)
        request.state.service = Service(params, ctx, self.__rds_plugins)
        return await call_next(request)
