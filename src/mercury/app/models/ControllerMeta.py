from dataclasses import dataclass
from typing import Any

from starlette.middleware import _MiddlewareClass

from mercury.core.Controller import Controller


@dataclass(frozen=True)
class ControllerMeta:
    path: str
    controller: type[Controller]
    middlewares: tuple[type[_MiddlewareClass[Any]]] | None
