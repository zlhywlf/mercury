from importlib import import_module
from importlib.resources import files
from importlib.resources.abc import Traversable
from types import ModuleType
from typing import Any, Generator


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


def find_class_by_type[T](module: ModuleType | None, super_type: T) -> T | None:
    """"""
    if not module or not isinstance(super_type, type):
        return None
    for clazz in module.__dict__.values():
        if not isinstance(clazz, type) or clazz is super_type or not issubclass(clazz, super_type):
            continue
        return clazz


async def run_dynamic_method(obj: object, name: str, *args: Any, **kwargs: Any) -> Any:
    """"""
    handler = getattr(obj, name)
    if not handler:
        raise RuntimeError(f"{name} not supported")
    return await handler(*args, **kwargs)
