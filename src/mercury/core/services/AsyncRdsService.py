from abc import ABC, abstractmethod


class AsyncRdsService(ABC):
    @abstractmethod
    def get_data(self):
        """"""
