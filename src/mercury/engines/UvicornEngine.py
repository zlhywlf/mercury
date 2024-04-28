from typing import Callable, override

import uvicorn

from mercury.engines.BaseEngine import BaseEngine


class UvicornEngine(BaseEngine):
    platform_type = ["Windows"]
    use_for_debug = True

    @override
    def launch(self) -> None:
        uvicorn.run(self._app)
