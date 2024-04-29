from mercury.controllers.BaseRdsController import BaseRdsController
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse


class TableController(BaseRdsController, HTTPEndpoint):
    @classmethod
    def path(cls) -> str:
        return "/rds/table/{id}"

    async def get(self, request: Request):
        return JSONResponse({'table': self.path()})

    async def post(self, request: Request):
        return self.get(request)
