from mercury.app.StarletteApp import StarletteApp
from mercury.controllers.starlette.rds.DataController import DataController
from mercury.controllers.starlette.rds.TableController import TableController
from mercury.middlewares.starlette.RdsMiddleware import RdsMiddleware

app = StarletteApp()
app.add_route(TableController.path(), TableController, middleware=[RdsMiddleware])
app.add_route(DataController.path(), DataController, middleware=[RdsMiddleware])
app.launch()
