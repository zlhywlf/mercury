from typing import override

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

from mercury.core.Application import Application
from mercury.utils.EncryptionUtil import encrypt_by_md5


class RdsMiddleware(BaseHTTPMiddleware):
    """"""

    def __init__(self, app: ASGIApp, application: Application) -> None:
        super().__init__(app)
        self._application = application

    @override
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        request.state.rds_config = self._application.rds_config
        # 参数解析
        path_params = request.path_params
        query_params = request.query_params
        json_params = await request.json()
        params = {**path_params, **query_params, **json_params}
        # 验证
        self.authentication(params.get('userId'),params.get('userKey'))
        return await call_next(request)

    async def parse_params(self, request: Request) -> dict:
        params = await request.json()
        # 获取 user key
        # 解析参数
        return params

    async def authentication(self, user_id: str, user_key: str, rds_key: str) -> bool:
        """"""
        return encrypt_by_md5(f"{user_id}+", rds_key) == user_key
