import platform
from typing import Any, Awaitable, Callable, MutableMapping, override

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.routing import Route

from mercury.app.EngineFactory import EngineFactory
from mercury.app.utils import yield_controllers
from mercury.core.Application import Application
from mercury.core.Context import Context
from mercury.core.Controller import Controller


class StarletteApp(Application):
    def __init__(self, *, context: Context, routes: list[type[Controller]]):
        super().__init__()
        self.__platform = platform.system()
        self.__has_launch = False
        self.__context = context
        self.__routes: list[Route] = [
            Route(
                path=meta.path,
                endpoint=meta.controller,
                middleware=[Middleware(_) for _ in (meta.middlewares or [])],
            )
            for meta in yield_controllers(routes)
        ]

    @override
    async def __call__(
        self,
        scope: MutableMapping[str, Any],
        receive: Callable[[], Awaitable[MutableMapping[str, Any]]],
        send: Callable[[MutableMapping[str, Any]], Awaitable[None]],
    ) -> None:
        """"""
        await Starlette(
            debug=self.context.setting.debug,
            lifespan=self.__context,
            routes=self.__routes,
        ).__call__(scope, receive, send)

    @property
    @override
    def platform(self) -> str:
        """"""
        return self.__platform

    @property
    @override
    def context(self) -> Context:
        """"""
        return self.__context

    @override
    def launch(self) -> None:
        """"""
        if not self.__has_launch:
            if not (engine := EngineFactory.create_engine(self)):
                raise RuntimeError("Starlette engine is not initialized")
            engine.launch()
            self.__has_launch = True
