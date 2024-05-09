from abc import ABC, abstractmethod
from typing import Self

from mercury.core.clients.Http import Http
from mercury.core.clients.Mongo import Mongo
from mercury.core.Plugin import Plugin
from mercury.core.Setting import Setting


class Context[T](ABC):

    def __init__(
        self, *, setting: Setting, http_client: Http, mongo_client: Mongo, rds_plugins: dict[str, type[Plugin]]
    ): ...

    @abstractmethod
    async def __aenter__(self) -> dict[str, Self]:
        """"""

    @abstractmethod
    async def __aexit__(self, *exc_info: object) -> None:
        """"""

    @abstractmethod
    def __call__(self, application: T) -> Self:
        """"""

    @property
    @abstractmethod
    def application(self) -> T:
        """"""

    @property
    @abstractmethod
    def http_client(self) -> Http:
        """"""

    @property
    @abstractmethod
    def mongo_client(self) -> Mongo:
        """"""

    @property
    @abstractmethod
    def rds_plugins(self) -> dict[str, type[Plugin]]:
        """"""

    @property
    @abstractmethod
    def setting(self) -> Setting:
        """"""

    @mongo_client.setter
    @abstractmethod
    def mongo_client(self, mongo_client: Mongo) -> None:
        """"""
