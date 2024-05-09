from abc import ABC, abstractmethod
from typing import Any, Awaitable, Callable, MutableMapping

from mercury.core.Context import Context
from mercury.core.Launch import Launch


class Application(Launch, ABC):

    def __init__(self, **kwargs): ...

    @abstractmethod
    async def __call__(
        self,
        scope: MutableMapping[str, Any],
        receive: Callable[[], Awaitable[MutableMapping[str, Any]]],
        send: Callable[[MutableMapping[str, Any]], Awaitable[None]],
    ) -> None:
        """"""

    @property
    @abstractmethod
    def platform(self) -> str:
        """"""

    @property
    @abstractmethod
    def context(self) -> Context:
        """"""
