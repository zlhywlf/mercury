from dataclasses import dataclass

from mercury.core.Controller import Controller


@dataclass
class ControllerMeta[T]:
    path: str
    controller: type[Controller]
    middlewares: list[T]
