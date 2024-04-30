from mercury.app.StarletteApp import StarletteApp
from mercury.controllers.starlette.rds.DataController import DataController
from mercury.controllers.starlette.rds.TableController import TableController
from mercury.middlewares.starlette.RdsMiddleware import RdsMiddleware

app = StarletteApp()
for path in TableController.path():
    app.add_route(path, TableController, middleware=[RdsMiddleware])
for path in DataController.path():
    app.add_route(path, DataController, middleware=[RdsMiddleware])
app.launch()
