from mercury.app.StarletteApp import StarletteApp
from mercury.controllers.starlette.rds.TableController import TableController
from mercury.controllers.starlette.rds.DataController import DataController

app = StarletteApp()
TableController.setup(app)
DataController.setup(app)
app.launch()
