from typing import override

import uvicorn

from mercury.core.BaseEngine import BaseEngine


class UvicornEngine(BaseEngine):

    @override
    def launch(self) -> None:
        uvicorn.run(self._application.instance)

    @classmethod
    @override
    def platforms(cls) -> list[str]:
        return ["Windows"]

    @classmethod
    @override
    def debug(cls) -> bool:
        return True
