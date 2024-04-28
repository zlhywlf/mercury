from typing import Callable, override

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Route

from mercury.core.Application import Application
from mercury.core.Setting import Setting
from mercury.engines.EngineFactory import EngineFactory
from mercury.settings.StarletteSetting import StarletteSetting


async def homepage(request: Request) -> Response:
    return JSONResponse({'hello': 'world'})


class StarletteApp(Application):

    def __init__(self):
        self._setting = StarletteSetting()

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
            routes=[Route('/', homepage, methods=['GET'])],
        )

    @property
    @override
    def setting(self) -> Setting:
        return self._setting
