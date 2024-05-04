from abc import ABC, abstractmethod
from typing import Any


class Http(ABC):
    """"""

    def __init__(self, **kwargs): ...

    @abstractmethod
    async def request(self, url: str, method: str, params: dict) -> Any:
        """"""

    @abstractmethod
    async def get(self, url: str, params: dict) -> Any:
        """"""
