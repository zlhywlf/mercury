from mercury.core.Application import Application
from mercury.core.Component import Component
from typing import override
from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse
from starlette.requests import Request


class BaseComponent(Component, HTTPEndpoint):
    """"""

    path = "/syx/data"
    path_param = "{app_id}"

    @classmethod
    @override
    def setup(cls, app: Application) -> None:
        app.add_route(f"{cls.path}/{cls.path_param}", cls)

    async def get(self, request: Request):
        return JSONResponse({'hello': self.path})

    async def post(self, request: Request):
        return self.get(request)

    def authentication(self):
        """"""
