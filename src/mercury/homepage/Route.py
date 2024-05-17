from typing import Any, override

from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from mercury.core.Controller import Controller


class Route(Controller, HTTPEndpoint):
    @classmethod
    @override
    def paths(cls) -> list[str]:
        return ["/"]

    @classmethod
    @override
    def middlewares(cls) -> tuple[Any] | None:
        return None

    async def get(self, request: Request) -> Response:
        return JSONResponse({"hostname": request.url.hostname})
