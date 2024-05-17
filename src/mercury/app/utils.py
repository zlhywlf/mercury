import hashlib
from importlib import import_module
from importlib.resources import files
from importlib.resources.abc import Traversable
from types import ModuleType
from typing import Any, Generator

from mercury.app.models.ControllerMeta import ControllerMeta
from mercury.core.Controller import Controller


def yield_controllers(
    controllers: list[type[Controller]],
) -> Generator[ControllerMeta, Any, None]:
    """"""
    for controller in controllers:
        paths = controller.paths()
        middlewares = controller.middlewares()
        for path in paths:
            yield ControllerMeta(path, controller, middlewares)


def get_modules(pkg: str) -> Generator[ModuleType | None, Any, None]:
    """"""

    def get_module(module_meta: Traversable) -> ModuleType | None:
        """"""
        name, point, suffix = module_meta.name.rpartition(".")
        if not module_meta.is_file() or suffix != "py":
            return None
        try:
            return import_module(f"{point}{name}", pkg)
        except ModuleNotFoundError as e:
            print(f"warning:{pkg}{point}{name}:{e}")
            return None

    return (get_module(module_meta) for module_meta in files(pkg).iterdir())


def find_class_by_type[T](module: ModuleType | None, super_type: T) -> T | None:  # type: ignore[valid-type,name-defined]
    """"""
    if not module or not isinstance(super_type, type):
        return None
    for cls in module.__dict__.values():
        if not isinstance(cls, type) or cls is super_type or not issubclass(cls, super_type):
            continue
        return cls
    return None


async def run_dynamic_method(obj: object, name: str, *args: Any, **kwargs: Any) -> Any:
    """"""
    handler = getattr(obj, name)
    if not handler:
        raise RuntimeError(f"{name} not supported")
    return await handler(*args, **kwargs)


def encrypt_by_md5(data: str, key: str) -> str:
    """"""
    return hashlib.md5(f"{data}{key}".encode("utf-8")).hexdigest()
