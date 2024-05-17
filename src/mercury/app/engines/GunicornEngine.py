import multiprocessing
from typing import Any, Self, override

from gunicorn.app.base import BaseApplication  # type: ignore[import-not-found]

from mercury.core.Application import Application
from mercury.core.Engine import Engine


class GunicornEngine(BaseApplication, Engine):  # type: ignore[misc]
    def __init__(self) -> None:
        self.__application: Application | None = None
        BaseApplication.__init__(self)

    @override
    def load(self) -> Application | None:  # type: ignore[misc]
        return self.__application

    @override
    def launch(self) -> None:
        self.run()

    @property
    def default_options(self) -> dict[str, Any]:
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
    def is_run_for_debug(cls) -> bool:
        return False

    @override
    def set_application(self, application: Application) -> Self:
        """"""
        self.__application = application
        return self

    @override
    def load_config(self) -> None:  # type: ignore[misc]
        """"""
        self.cfg.set("bind", "0.0.0.0:8000")
        self.cfg.set("workers", multiprocessing.cpu_count() * 2 + 1)
        self.cfg.set("worker_class", "uvicorn.workers.UvicornWorker")
        self.cfg.set("backlog", 64)
        self.cfg.set("worker_connections", 1000)
        self.cfg.set("max_requests", 5000)
        self.cfg.set("max_requests_jitter", 100)
        self.cfg.set("timeout", 7200)
        self.cfg.set("reload", "false")
