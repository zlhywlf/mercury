from abc import ABC, abstractmethod
from typing import Any

from mercury.core.Client import Client
from mercury.core.Close import Close


class HttpClient[CLIENT, RESPONSE](Close, Client[CLIENT], ABC):  # type: ignore[valid-type,name-defined,type-arg]
    @abstractmethod
    async def request(self, url: str, method: str, params: dict[str, Any]) -> RESPONSE:  # type: ignore[name-defined]
        """"""

    @abstractmethod
    async def get(self, url: str, params: dict[str, Any]) -> RESPONSE:  # type: ignore[name-defined]
        """"""

    @abstractmethod
    async def post(self, url: str, params: dict[str, Any]) -> RESPONSE:  # type: ignore[name-defined]
        """"""
