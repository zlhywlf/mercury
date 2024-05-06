import contextlib
import platform
from typing import Any, AsyncGenerator, Self, override

from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.responses import JSONResponse
from starlette.routing import Route

from mercury.clients.HttpHttpx import HttpHttpx
from mercury.clients.MongoMotor import MongoMotor
from mercury.core.Application import Application
from mercury.core.Controller import Controller
from mercury.core.Plugin import Plugin
from mercury.core.Setting import Setting
from mercury.factories.EngineFactory import EngineFactory
from mercury.models.AppContext import AppContext
from mercury.utils.ControllerUtil import yield_controllers


class StarletteApplication(Starlette, Application):

    def __init__(self, *, setting: Setting, controllers: list[type[Controller]], rds_plugins: dict[str, type[Plugin]]):
        self.__setting = setting
        self.__platform = platform.system()
        self.__rds_plugins = rds_plugins
        routes: list[Route] = [Route('/', lambda request: JSONResponse({'hello': 'world'}), methods=['GET'])]
        for meta in yield_controllers(controllers):
            routes.append(Route(meta.path, meta.controller, middleware=[Middleware(_) for _ in meta.middlewares]))
        Starlette.__init__(self, debug=setting.is_debug, lifespan=self.lifespan, routes=routes)

    @override
    def launch(self) -> None:
        if not (engine := EngineFactory.create_engine(self)):
            raise RuntimeError('Starlette engine is not initialized')
        engine.launch()

    @property
    @override
    def setting(self) -> Setting:
        return self.__setting

    @property
    @override
    def platform(self) -> str:
        return self.__platform

    @contextlib.asynccontextmanager
    async def lifespan(self, app: Self) -> AsyncGenerator[dict[str, AppContext], Any]:
        async with AsyncClient() as http_client:
            yield {"ctx": AppContext(HttpHttpx(client=http_client),
                                     app,
                                     MongoMotor(AsyncIOMotorClient(self.setting.mongo)),
                                     self.__rds_plugins)
                   }
