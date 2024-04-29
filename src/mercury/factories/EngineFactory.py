import mercury.engines
from mercury.core.Application import Application
from mercury.core.BaseEngine import BaseEngine
from mercury.utils.ModuleUtil import find_class_by_type, get_modules


class EngineFactory:

    @staticmethod
    def create_engine(application: Application) -> BaseEngine | None:
        platform = application.platform
        is_debug = application.setting.is_debug

        for m in get_modules(mercury.engines.__name__):
            if clazz := find_class_by_type(m, BaseEngine):
                if is_debug:
                    if clazz.debug():
                        return clazz(application)
                else:
                    if platform in clazz.platforms():
                        return clazz(application)
        return None
