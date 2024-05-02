import platform
from typing import Callable, override

from motor.motor_asyncio import AsyncIOMotorDatabase
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.responses import JSONResponse
from starlette.routing import BaseRoute, Route

from mercury.core.Application import Application
from mercury.core.Setting import Setting
from mercury.factories.EngineFactory import EngineFactory


class StarletteApplication(Application):

    def __init__(self, *, setting: Setting, async_db: AsyncIOMotorDatabase):
        self._setting = setting
        self._routes: list[BaseRoute] = []
        self._platform = platform.system()
        self._app: Starlette | None = None
        self._async_db = async_db

    @override
    def launch(self) -> None:
        if not (engine := EngineFactory.create_engine(self)):
            raise RuntimeError('Starlette engine is not initialized')
        engine.launch()

    @property
    @override
    def instance(self) -> Callable:
        if not self._app:
            self._app = Starlette(
                debug=self._setting.is_debug,
                routes=[Route('/', lambda request: JSONResponse({'hello': 'world'}), methods=['GET']), *self._routes],
            )
        return self._app

    @property
    @override
    def setting(self) -> Setting:
        return self._setting

    @override
    def add_route(self, path: str, endpoint: Callable, **kwargs) -> None:
        if not self._app:
            middlewares = kwargs.pop("middlewares", [])
            self._routes.append(
                Route(path, endpoint,
                      middleware=[Middleware(_, application=self, async_db=self._async_db) for _ in middlewares],
                      **kwargs))

    @property
    @override
    def platform(self) -> str:
        return self._platform

    @property
    @override
    def rds_config(self) -> dict[str, dict]:
        return {
            "table01": {
                "id": "table01",
                "type": "task",
                "pre": None,
                "post": None,
                "parent": None,
                "orderNo": "NO123",
                "args": [
                    {
                        "name": "name",
                        "type": "string",
                        "from": "name",
                        "required": True,
                        "default": "default",
                    },
                    {
                        "name": "age",
                        "type": "integer",
                        "from": "age",
                        "required": True,
                        "default": "default",
                    },
                    {
                        "name": "needAll",
                        "type": "bool",
                        "from": "needAll",
                        "required": False,
                        "default": "False",
                    }
                ],
                "objects": [
                    {
                        "id": "http://127.0.0.1:8000/rds/data",
                        "type": "api",
                        "args": None,
                        "pre": None,
                        "parent": "NO123",
                        "orderNo": None,
                        "post": [
                            {
                                "id": "inner",
                                "type": "func",
                                "args": None,
                                "pre": None,
                                "post": None,
                                "objects": None,
                            }
                        ],
                        "objects": None,
                    }
                ],

            },
            "data01": {
                "id": "data01",
                "type": "task",
                "pre": None,
                "post": None,
                "parent": None,
                "orderNo": "NO123",
                "args": [
                    {
                        "name": "name",
                        "type": "string",
                        "from": "name",
                        "required": True,
                        "default": "default",
                    },
                    {
                        "name": "age",
                        "type": "integer",
                        "from": "age",
                        "required": True,
                        "default": "default",

                    }
                ],
                "objects": [{
                    "id": "name",
                    "type": "other",
                    "pre": None,
                    "post": None,
                    "parent": "NO123",
                    "orderNo": "NO123name",
                    "objects": [
                        {
                            "id": "table01",
                            "type": "table",
                            "args": [
                                {
                                    "name": "name",
                                    "type": "string",
                                    "from": "name",
                                    "required": True,
                                    "default": "default",
                                },
                                {
                                    "name": "age",
                                    "type": "integer",
                                    "from": "age",
                                    "required": True,
                                    "default": "default",
                                }
                            ],
                            "pre": None,
                            "post": None,
                            "parent": "NO123name",
                            "orderNo": "None",
                            "objects": [
                                {
                                    "id": "name_sub",
                                    "type": "l1",
                                    "pre": None,
                                    "post": None,
                                    "parent": "None",
                                    "orderNo": "None",
                                    "objects": [
                                        {
                                            "id": "table01",
                                            "type": "table",
                                            "parent": "None",
                                            "orderNo": "None",
                                            "args": [
                                                {
                                                    "name": "name",
                                                    "type": "string",
                                                    "from": "name_sub"
                                                },
                                                {
                                                    "name": "age",
                                                    "type": "integer",
                                                    "from": "age_age"
                                                }
                                            ],
                                            "pre": None,
                                            "post": None,
                                            "objects": None
                                        }
                                    ]
                                },

                            ]
                        }
                    ]
                }],
            }}
