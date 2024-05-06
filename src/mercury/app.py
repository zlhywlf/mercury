import mercury.plugins
from mercury.applications.StarletteApplication import StarletteApplication
from mercury.builders.ApplicationBuilder import ApplicationBuilder
from mercury.controllers.starlette.rds.RdsController import RdsController
from mercury.settings.StarletteSetting import StarletteSetting

app = ApplicationBuilder(StarletteApplication).add_rds_plugins(mercury.plugins.__name__).add_setting(
    StarletteSetting()).add_controllers(RdsController).build()
