from typing import Self, override

import uvicorn

from mercury.core.Application import Application
from mercury.core.Engine import Engine


class UvicornEngine(Engine):
    def __init__(self) -> None:
        self.__application: Application | None = None

    @override
    def launch(self) -> None:
        if self.__application:
            uvicorn.run(self.__application)
        else:
            raise RuntimeError("the application is None")

    @classmethod
    @override
    def platforms(cls) -> list[str]:
        return ["Windows"]

    @classmethod
    @override
    def is_run_for_debug(cls) -> bool:
        return True

    @override
    def set_application(self, application: Application) -> Self:
        """"""
        self.__application = application
        return self
