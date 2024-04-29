from mercury.controllers.BaseRdsController import BaseRdsController
from typing import override
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse


class DataController(BaseRdsController, HTTPEndpoint):
    @classmethod
    @override
    def path(cls) -> str:
        return "/rds/data/{id}"

    async def get(self, request: Request):
        return JSONResponse({'data': self.path()})

    async def post(self, request: Request):
        return self.get(request)
