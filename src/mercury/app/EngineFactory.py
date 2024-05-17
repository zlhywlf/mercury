import mercury.app.engines
from mercury.app.utils import find_class_by_type, get_modules
from mercury.core.Application import Application
from mercury.core.Engine import Engine


class EngineFactory:
    @staticmethod
    def create_engine(application: Application) -> Engine | None:
        platform = application.platform
        is_debug = application.context.setting.debug

        for m in get_modules(mercury.app.engines.__name__):
            if cls := find_class_by_type(m, Engine):
                if is_debug:
                    if cls.is_run_for_debug():
                        return cls().set_application(application)  # type: ignore[no-any-return]
                else:
                    if platform in cls.platforms():
                        return cls().set_application(application)  # type: ignore[no-any-return]
        return None
