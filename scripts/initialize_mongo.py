import asyncio

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from mercury.settings.StarletteSetting import StarletteSetting


async def initialize_task_table(tbl_name: str, db: AsyncIOMotorDatabase) -> None:
    """"""
    await asyncio.sleep(1)
    print("initialize_task_table")


async def main() -> None:
    """"""
    setting = StarletteSetting("../.env")
    db = AsyncIOMotorClient(setting.mongo)[setting.project_name]
    await asyncio.gather(
        asyncio.create_task(initialize_task_table(setting.rds_task_table_name, db)),
    )


if __name__ == "__main__":
    asyncio.run(main())
