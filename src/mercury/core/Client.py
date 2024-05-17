from abc import ABC, abstractmethod


class Client[CLIENT](ABC):  # type: ignore[valid-type]
    @property
    @abstractmethod
    def client(self) -> CLIENT:  # type: ignore[name-defined]
        """"""

    @client.setter
    @abstractmethod
    def client(self, client: CLIENT) -> None:  # type: ignore[name-defined]
        """"""
