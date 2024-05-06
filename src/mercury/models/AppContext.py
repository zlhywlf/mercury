from dataclasses import dataclass

from mercury.core.Application import Application
from mercury.core.clients.Http import Http
from mercury.core.clients.Mongo import Mongo
from mercury.core.Plugin import Plugin


@dataclass(frozen=True)
class AppContext:
    http_client: Http
    application: Application
    mongo_client: Mongo
    rds_plugins: dict[str, type[Plugin]]
