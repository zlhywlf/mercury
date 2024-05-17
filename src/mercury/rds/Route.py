import time
from typing import Any, override

import orjson
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from mercury.core.Controller import Controller
from mercury.rds.Middleware import Middleware
from mercury.rds.Service import Service


class OrjsonResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        return orjson.dumps(content)


class Route(Controller, HTTPEndpoint):
    @classmethod
    @override
    def paths(cls) -> list[str]:
        return ["/rds", "/rds/{appId}"]

    @classmethod
    @override
    def middlewares(cls) -> tuple[type[Middleware]]:
        return (Middleware,)

    async def get(self, request: Request) -> Response:
        s = time.time()
        service: Service = request.state.service
        await service.get_data()
        data = service.content.model_dump()
        e = time.time()
        return OrjsonResponse(
            {
                "class": service.app_id,
                "code": data.get("code"),
                "msg": data.get("msg"),
                "elapse": e - s,
                "contents": data.get("data"),
            }
        )

    async def post(self, request: Request) -> Response:
        return await self.get(request)
