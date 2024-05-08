from abc import ABC, abstractmethod

from mercury.core.Setting import Setting


class Mongo[T](ABC):
    """"""

    def __init__(self, setting: Setting): ...

    @abstractmethod
    async def get_db_by_name(self, name: str) -> T:
        """"""

    @abstractmethod
    async def close(self) -> None:
        """"""
