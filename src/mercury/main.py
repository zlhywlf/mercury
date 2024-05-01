from mercury.applications.StarletteApplication import StarletteApplication
from mercury.controllers.starlette.rds.DataController import DataController
from mercury.controllers.starlette.rds.TableController import TableController
from mercury.middlewares.starlette.RdsMiddleware import RdsMiddleware

starlette_app = StarletteApplication()
for path in TableController.path():
    starlette_app.add_route(path, TableController, middleware=[RdsMiddleware])
for path in DataController.path():
    starlette_app.add_route(path, DataController, middleware=[RdsMiddleware])
