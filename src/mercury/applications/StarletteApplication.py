import platform
from typing import Callable, override, AsyncIterator, TypedDict

from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorDatabase
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.responses import JSONResponse
from starlette.routing import BaseRoute, Route

from mercury.core.Application import Application
from mercury.core.Setting import Setting
from mercury.factories.EngineFactory import EngineFactory
import contextlib


class StarletteApplication(Application):

    def __init__(self, *, setting: Setting, async_db: AsyncIOMotorDatabase):
        self.__setting = setting
        self.__routes: list[BaseRoute] = []
        self.__platform = platform.system()
        self.__app: Starlette | None = None
        self.__async_db = async_db

    @override
    def launch(self) -> None:
        if not (engine := EngineFactory.create_engine(self)):
            raise RuntimeError('Starlette engine is not initialized')
        engine.launch()

    @property
    @override
    def instance(self) -> Callable:
        if not self.__app:
            self.__app = Starlette(
                debug=self.__setting.is_debug,
                lifespan=StarletteApplication.lifespan,
                routes=[Route('/', lambda request: JSONResponse({'hello': 'world'}), methods=['GET']), *self.__routes],
            )
        return self.__app

    @property
    @override
    def setting(self) -> Setting:
        return self.__setting

    @override
    def add_route(self, path: str, endpoint: Callable, **kwargs) -> None:
        if not self.__app:
            middlewares = kwargs.pop("middlewares", [])
            self.__routes.append(
                Route(path, endpoint,
                      middleware=[Middleware(_, application=self, async_db=self.__async_db) for _ in middlewares],
                      **kwargs))

    @property
    @override
    def platform(self) -> str:
        return self.__platform

    @staticmethod
    @contextlib.asynccontextmanager
    async def lifespan(app: Starlette) -> AsyncIterator[dict[str, AsyncClient]]:
        async with AsyncClient() as client:
            yield {"http_client": client}
