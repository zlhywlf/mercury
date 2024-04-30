from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse

from mercury.core.Controller import Controller


class TableController(Controller, HTTPEndpoint):

    @classmethod
    def path(cls) -> list[str]:
        return ["/rds/table", "/rds/table/{id}"]

    async def get(self, request: Request):
        rds_config = request.state.rds_config
        rds_config.append(888)
        return JSONResponse({'table': rds_config})

    async def post(self, request: Request):
        return self.get(request)
