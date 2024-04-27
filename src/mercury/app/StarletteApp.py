from typing import Callable, override

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Route

from mercury.core.Application import Application
from mercury.core.Setting import Setting
from mercury.engines.EngineFactory import EngineFactory


async def homepage(request: Request) -> Response:
    return JSONResponse({'hello': 'world'})


class StarletteApp(Application):

    def __init__(self, setting: Setting):
        self._setting = setting
        if not (engine := EngineFactory.create_engine(self, setting)):
            raise RuntimeError('Starlette engine is not initialized')
        self._engine = engine

    @override
    def launch(self) -> None:
        self._engine.launch()

    @property
    @override
    def app(self) -> Callable:
        return Starlette(
            debug=self._setting.is_debug,
            routes=[Route('/', homepage, methods=['GET'])],
        )
