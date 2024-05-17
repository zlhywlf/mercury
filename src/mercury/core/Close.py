from abc import ABC, abstractmethod


class Close(ABC):
    @abstractmethod
    async def close(self) -> None:
        """"""
