import multiprocessing
from typing import override

from gunicorn.app.base import BaseApplication

from mercury.core.Application import Application
from mercury.core.BaseEngine import BaseEngine


class GunicornEngine(BaseApplication, BaseEngine):

    def __init__(self, application: Application, options: dict | None = None) -> None:
        self.__options = self.default_options | (options or {})
        BaseEngine.__init__(self, application)
        BaseApplication.__init__(self)

    @override
    def load_config(self):
        config = {key: value for key, value in self.__options.items() if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    @override
    def load(self):
        return self._application.instance

    @override
    def launch(self) -> None:
        self.run()

    @property
    def default_options(self) -> dict:
        return {
            "workers": multiprocessing.cpu_count() * 2 + 1,
            "worker_class": "uvicorn.workers.UvicornWorker",
        }

    @classmethod
    @override
    def platforms(cls) -> list[str]:
        return ["Linux", "Darwin"]

    @classmethod
    @override
    def debug(cls) -> bool:
        return False
