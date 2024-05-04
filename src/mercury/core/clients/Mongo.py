from abc import ABC, abstractmethod


class Mongo(ABC):
    """"""

    def __init__(self, **kwargs): ...

    @abstractmethod
    def get_db_by_name(self, name: str):
        """"""
