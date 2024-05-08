from abc import ABC, abstractmethod
from typing import Any

from mercury.core.Setting import Setting


class Http[T](ABC):
    """"""

    def __init__(self, setting: Setting): ...

    @abstractmethod
    async def request(self, url: str, method: str, params: dict) -> Any:
        """"""

    @abstractmethod
    async def get(self, url: str, params: dict) -> Any:
        """"""

    @abstractmethod
    async def post(self, url: str, params: dict) -> Any:
        """"""

    @abstractmethod
    async def close(self) -> None:
        """"""

    @property
    @abstractmethod
    def client(self) -> T:
        """"""

    @client.setter
    @abstractmethod
    def client(self, client: T) -> None:
        """"""
