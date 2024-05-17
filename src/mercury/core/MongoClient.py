from abc import ABC, abstractmethod
from typing import Any

from mercury.core.Client import Client
from mercury.core.Close import Close


class MongoClient[CLIENT](Close, Client[CLIENT], ABC):  # type: ignore[valid-type,name-defined,type-arg]
    @abstractmethod
    async def find_one(self, table_name: str, query: dict[str, Any]) -> Any:
        """"""
