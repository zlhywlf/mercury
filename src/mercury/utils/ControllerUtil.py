from typing import Any, Generator

from mercury.core.Controller import Controller
from mercury.models.ControllerMeta import ControllerMeta


def yield_controllers(controllers: list[type[Controller]]) -> Generator[ControllerMeta, Any, None]:
    """"""
    for controller in controllers:
        paths = controller.paths()
        middlewares = controller.middlewares()
        for path in paths:
            yield ControllerMeta(path, controller, middlewares)
