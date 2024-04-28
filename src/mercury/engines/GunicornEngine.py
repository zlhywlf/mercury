import multiprocessing
from typing import Callable, override

from gunicorn.app.base import BaseApplication

from mercury.core.Engine import Engine


class GunicornEngine(BaseApplication, Engine):

    def __init__(self, app: Callable, options: dict | None = None) -> None:
        self._options = self.default_options | (options or {})
        self._app = app
        BaseApplication.__init__(self)

    @override
    def load_config(self):
        config = {key: value for key, value in self._options.items() if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    @override
    def load(self):
        return self._app

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
