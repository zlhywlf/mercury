from dataclasses import dataclass

from mercury.core.Application import Application
from mercury.core.clients.Http import Http
from mercury.core.clients.Mongo import Mongo


@dataclass
class AppContext:
    http_client: Http
    application: Application
    mongo_client: Mongo
