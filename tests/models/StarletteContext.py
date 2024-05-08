from dataclasses import dataclass

from starlette.testclient import TestClient

from mercury.core.clients.Mongo import Mongo
from mercury.core.Setting import Setting


@dataclass
class StarletteContext:
    client: TestClient
    rds_auth: dict[str, str]
    db: Mongo
    setting: Setting
