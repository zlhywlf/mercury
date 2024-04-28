from typing import Callable, override

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Route

from mercury.core.Application import Application
from mercury.core.Setting import Setting
from mercury.factories.EngineFactory import EngineFactory
from mercury.settings.StarletteSetting import StarletteSetting
from starlette.endpoints import HTTPEndpoint
from mercury.utils.DecoratorUtil import authentication
from starlette.routing import BaseRoute


class Homepage(HTTPEndpoint):

    @authentication
    async def get(self, request):
        return JSONResponse({'hello': 'world'})


async def handle_data(request: Request) -> Response:
    # data_id = request.path_params['data_id']
    data_id = await request.json()
    return JSONResponse({'data_id': data_id})


class StarletteApp(Application):

    def __init__(self):
        self._setting = StarletteSetting()
        self._routes: list[BaseRoute] = []

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
        self._routes.append(Route(path, endpoint, **kwargs))
