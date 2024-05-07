import asyncio
import json

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from mercury.models.rds.Task import Task
from mercury.settings.StarletteSetting import StarletteSetting


async def initialize_task_table(tbl_name: str, db: AsyncIOMotorDatabase) -> None:
    """"""
    with open("rds_task.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        data = [Task(**_).model_dump() for _ in data]
        await db[tbl_name].insert_many(data)


async def main() -> None:
    """"""
    setting = StarletteSetting("../.env")
    db = AsyncIOMotorClient(setting.mongo)[setting.project_name]
    await asyncio.gather(
        asyncio.create_task(initialize_task_table(setting.rds_task_table_name, db)),
    )


if __name__ == "__main__":
    asyncio.run(main())
