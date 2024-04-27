from typing import Callable, override

import uvicorn

from mercury.engines.BaseEngine import BaseEngine


class UvicornEngine(BaseEngine):
    platform_type = ["Windows"]
    use_for_debug = True

    def __init__(self, app: Callable):
        super().__init__(app)

    @override
    def launch(self) -> None:
        uvicorn.run(self._app)
