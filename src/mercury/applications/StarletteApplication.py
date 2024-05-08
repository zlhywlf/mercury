import platform
from typing import Any, Awaitable, Callable, MutableMapping, override

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.responses import JSONResponse
from starlette.routing import Route

from mercury.core.Application import Application
from mercury.core.Context import Context
from mercury.core.Controller import Controller
from mercury.core.Setting import Setting
from mercury.factories.EngineFactory import EngineFactory
from mercury.utils.ControllerUtil import yield_controllers


class StarletteApplication(Application):

    def __init__(self, *, lifespan: Context, setting: Setting, controllers: list[type[Controller]], ):
        super().__init__()
        self.__setting = setting
        self.__platform = platform.system()
        self.__has_launch = False
        self.__context = lifespan
        self.__routes: list[Route] = [Route('/', lambda request: JSONResponse({'hello': 'world'}), methods=['GET'])]
        for meta in yield_controllers(controllers):
            self.__routes.append(
                Route(meta.path, meta.controller, middleware=[Middleware(_) for _ in meta.middlewares]))

    @override
    def launch(self) -> None:
        if not self.__has_launch:
            if not (engine := EngineFactory.create_engine(self)):
                raise RuntimeError('Starlette engine is not initialized')
            engine.launch()
            self.__has_launch = True

    @property
    @override
    def setting(self) -> Setting:
        return self.__setting

    @property
    @override
    def platform(self) -> str:
        return self.__platform

    @property
    @override
    def context(self) -> Context:
        """"""
        return self.__context

    @override
    async def __call__(self, scope: MutableMapping[str, Any],
                       receive: Callable[[], Awaitable[MutableMapping[str, Any]]],
                       send: Callable[[MutableMapping[str, Any]], Awaitable[None]]) -> None:
        """"""
        await Starlette(
            debug=self.__setting.is_debug,
            lifespan=self.__context,
            routes=self.__routes).__call__(scope, receive, send)
