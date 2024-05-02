from dataclasses import dataclass

from motor.motor_asyncio import AsyncIOMotorDatabase
from starlette.testclient import TestClient


@dataclass
class StarletteContext:
    client: TestClient
    rds_auth: dict[str, str]
    db: AsyncIOMotorDatabase
