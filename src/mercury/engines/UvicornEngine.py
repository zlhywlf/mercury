from typing import Callable, override

import uvicorn

from mercury.core.Engine import Engine


class UvicornEngine(Engine):

    def __init__(self, app: Callable) -> None:
        self._app = app

    @override
    def launch(self) -> None:
        uvicorn.run(self._app)

    @classmethod
    @override
    def platforms(cls) -> list[str]:
        return ["Windows"]

    @classmethod
    @override
    def debug(cls) -> bool:
        return True
