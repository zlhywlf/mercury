import platform
from typing import Callable, override

from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.middleware import Middleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import BaseRoute, Route

from mercury.core.Application import Application
from mercury.core.Setting import Setting
from mercury.factories.EngineFactory import EngineFactory
from mercury.settings.StarletteSetting import StarletteSetting
from mercury.utils.DecoratorUtil import authentication


class Homepage(HTTPEndpoint):

    @authentication
    async def get(self, request: Request) -> Response:
        return JSONResponse({'hello': 'world'})


class StarletteApp(Application):

    def __init__(self):
        self._setting = StarletteSetting()
        self._routes: list[BaseRoute] = []
        self._platform = platform.system()

    @override
    def launch(self) -> None:
        if not (engine := EngineFactory.create_engine(self)):
            raise RuntimeError('Starlette engine is not initialized')
        engine.launch()

    @property
    @override
    def app(self) -> Callable:
        return Starlette(
            debug=self._setting.is_debug,
            routes=[Route('/', Homepage, methods=['GET']), *self._routes],
        )

    @property
    @override
    def setting(self) -> Setting:
        return self._setting

    @override
    def add_route(self, path: str, endpoint: Callable, **kwargs) -> None:
        middleware = kwargs.pop("middleware", [])
        self._routes.append(
            Route(path, endpoint, middleware=[Middleware(_, application=self) for _ in middleware], **kwargs))

    @property
    @override
    def platform(self) -> str:
        return self._platform

    @property
    @override
    def rds_config(self) -> list:
        return [1, 2, 3]
