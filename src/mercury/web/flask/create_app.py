"""创建 app"""

from flask import Flask

app = Flask("mercury")


@app.route("/")
def hello_world() -> str:
    """hello world

    Returns:
        str: hello world
    """
    return "<h1>Hello, World!</h1>"
