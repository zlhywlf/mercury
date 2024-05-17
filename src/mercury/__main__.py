from mercury.app.clients.HttpxClient import HttpxClient
from mercury.app.clients.MotorClient import MotorClient
from mercury.app.ProjectSetting import ProjectSetting
from mercury.app.StarletteApp import StarletteApp
from mercury.app.StarletteContext import StarletteContext
from mercury.homepage.Route import Route as HomePageRoute
from mercury.rds.Route import Route as RdsRoute

setting = ProjectSetting()
ctx = StarletteContext(setting=setting, http_client=HttpxClient(setting), mongo_client=MotorClient(setting))
routes = [HomePageRoute, RdsRoute]
app = StarletteApp(context=ctx, routes=routes)


def main() -> None:
    app.launch()


if __name__ == "__main__":
    main()
