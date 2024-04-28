from mercury.core.Application import Application
from mercury.core.Component import Component
from mercury.core.Setting import Setting
from typing import override
from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse, Response
from starlette.requests import Request
import functools


class BaseComponent(Component):
    """"""
    path = "/component/data/{id}"

    @override
    def setup(self, app: Application, setting: Setting) -> None:
        app.add_route(self.path, BaseComponent.Data)

    class Data(HTTPEndpoint):

        async def get(self, request: Request):
            return JSONResponse({'hello': 'world'})
