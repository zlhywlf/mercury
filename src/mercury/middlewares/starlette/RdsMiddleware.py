from typing import override

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

from mercury.core.Application import Application


class RdsMiddleware(BaseHTTPMiddleware):
    """"""

    def __init__(self, app: ASGIApp, application: Application) -> None:
        super().__init__(app)
        self._application = application

    @override
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        request.state.rds_config = self._application.rds_config
        return await call_next(request)

    async def parse_params(self, request: Request) -> dict:
        params = await request.json()
        return params

    async def authentication(self, user_id: str, user_key: str) -> bool:
        """"""
