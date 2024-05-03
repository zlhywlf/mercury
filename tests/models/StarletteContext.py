from dataclasses import dataclass

from motor.motor_asyncio import AsyncIOMotorDatabase
from starlette.testclient import TestClient

from mercury.core.Setting import Setting


@dataclass
class StarletteContext:
    client: TestClient
    rds_auth: dict[str, str]
    db: AsyncIOMotorDatabase
    setting: Setting
