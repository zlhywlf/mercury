import mercury.plugins
from mercury.applications.StarletteApplication import StarletteApplication
from mercury.builders.ApplicationBuilder import ApplicationBuilder
from mercury.clients.HttpHttpx import HttpHttpx
from mercury.clients.MongoMotor import MongoMotor
from mercury.contexts.StarletteContext import StarletteContext
from mercury.controllers.starlette.rds.RdsController import RdsController
from mercury.settings.StarletteSetting import StarletteSetting

setting = StarletteSetting()
mongo_client = MongoMotor(setting)
http_client = HttpHttpx(setting)
app = (
    ApplicationBuilder(StarletteApplication, StarletteContext)
    .add_rds_plugins(mercury.plugins.__name__)
    .add_setting(setting)
    .add_http_client(http_client)
    .add_mongo_client(mongo_client)
    .add_controllers(RdsController)
    .build()
)
