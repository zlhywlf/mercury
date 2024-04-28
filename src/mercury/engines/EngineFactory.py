import platform
from importlib import import_module
from importlib.resources import files
from importlib.resources.abc import Traversable
from types import ModuleType

import mercury.engines
from mercury.core.Application import Application
from mercury.core.Engine import Engine
from mercury.engines.BaseEngine import BaseEngine


class EngineFactory:

    @staticmethod
    def create_engine(application: Application) -> Engine | None:
        pkg = mercury.engines.__name__
        platform_type = platform.system()
        app = application.app
        is_debug = application.setting.is_debug

        for engine in files(pkg).iterdir():
            if not (m := EngineFactory.__get_engine_module(engine, pkg)):
                continue
            if clazz := EngineFactory.__get_engine(m, platform_type, is_debug):
                return clazz(app)
        return None

    @staticmethod
    def __get_engine(module: ModuleType, platform_type: str, is_debug: bool) -> type | None:
        for clazz in module.__dict__.values():
            if not isinstance(clazz, type) or clazz is BaseEngine or not issubclass(clazz, BaseEngine):
                continue
            if is_debug:
                return clazz if clazz.use_for_debug else None
            return clazz if platform_type in clazz.platform_type else None

    @staticmethod
    def __get_engine_module(engine: Traversable, pkg: str) -> ModuleType | None:
        name, point, suffix = engine.name.rpartition('.')
        if not engine.is_file() or suffix != "py":
            return None
        try:
            return import_module(f"{point}{name}", pkg)
        except ModuleNotFoundError as e:
            print(f"warning:{pkg}{point}{name}:{e}")
            return None
