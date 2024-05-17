from abc import ABC, abstractmethod
from typing import Self

from mercury.core.HttpClient import HttpClient
from mercury.core.MongoClient import MongoClient
from mercury.core.Setting import Setting


class Context[APP](ABC):  # type: ignore[valid-type]
    @abstractmethod
    async def __aenter__(self) -> dict[str, Self]:
        """"""

    @abstractmethod
    async def __aexit__(self, *exc_info: object) -> None:
        """"""

    @abstractmethod
    def __call__(self, application: APP) -> Self:  # type: ignore[name-defined]
        """"""

    @property
    @abstractmethod
    def application(self) -> APP | None:  # type: ignore[name-defined]
        """"""

    @property
    @abstractmethod
    def http_client(self) -> HttpClient:
        """"""

    @property
    @abstractmethod
    def mongo_client(self) -> MongoClient:
        """"""

    @mongo_client.setter
    @abstractmethod
    def mongo_client(self, mongo_client: MongoClient) -> None:
        """"""

    @property
    @abstractmethod
    def setting(self) -> Setting:
        """"""
