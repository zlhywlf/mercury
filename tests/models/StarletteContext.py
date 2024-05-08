from dataclasses import dataclass

from httpx import AsyncClient

from mercury.core.clients.Mongo import Mongo
from mercury.core.Setting import Setting


@dataclass
class StarletteContext:
    client: AsyncClient
    rds_auth: dict[str, str]
    db: Mongo
    setting: Setting
