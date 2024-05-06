from abc import ABC, abstractmethod

from mercury.core.clients.Http import Http
from mercury.core.clients.Mongo import Mongo
from mercury.models.rds.Content import Content
from mercury.models.rds.PluginMeta import PluginMeta
from mercury.models.rds.Task import Task


class Plugin(ABC):
    def __init__(self, meta: PluginMeta, http_client: Http, mongo_client: Mongo):
        """"""

    def pre(self, current: Content, parent: Content, rds_task: Task) -> None:
        """"""

    def post(self, current: Content, parent: Content, rds_task: Task) -> None:
        """"""

    @classmethod
    @abstractmethod
    def plugin_id(cls) -> str:
        """"""
