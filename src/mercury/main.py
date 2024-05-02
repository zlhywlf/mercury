from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from mercury.applications.StarletteApplication import StarletteApplication
from mercury.controllers.starlette.rds.RdsController import RdsController
from mercury.middlewares.starlette.RdsMiddleware import RdsMiddleware
from mercury.settings.StarletteSetting import StarletteSetting


def create_async_db(url: str) -> AsyncIOMotorDatabase:
    return AsyncIOMotorClient(url)["mercury"]


def create_setting() -> StarletteSetting:
    return StarletteSetting()


def create_starlette_app(setting: StarletteSetting, async_db: AsyncIOMotorDatabase) -> StarletteApplication:
    starlette_app = StarletteApplication(setting=setting, async_db=async_db)
    for path in RdsController.path():
        starlette_app.add_route(path, RdsController, middleware=[RdsMiddleware])
    return starlette_app
