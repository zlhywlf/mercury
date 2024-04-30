from typing import override

from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse

from mercury.core.Controller import Controller


class DataController(Controller, HTTPEndpoint):

    @classmethod
    @override
    def path(cls) -> list[str]:
        return ["/rds/data", "/rds/data/{id}"]

    async def get(self, request: Request):
        rds_config = request.state.rds_config
        rds_config.append(999)
        return JSONResponse({'data': rds_config})

    async def post(self, request: Request):
        return self.get(request)
