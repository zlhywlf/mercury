from mercury.app.StarletteApp import StarletteApp
from mercury.components.BaseComponent import BaseComponent

app = StarletteApp()
BaseComponent.setup(app)
app.launch()
