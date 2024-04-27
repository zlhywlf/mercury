from mercury.app.StarletteApp import StarletteApp
from mercury.settings.StarletteSetting import StarletteSetting

setting = StarletteSetting()
app = StarletteApp(setting)

app.launch()
