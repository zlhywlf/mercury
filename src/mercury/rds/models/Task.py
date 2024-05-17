from datetime import datetime

from pydantic import BaseModel, Field, computed_field

from mercury.rds.models.Config import Config
from mercury.rds.models.PluginMeta import PluginMeta


class Task(BaseModel):
    key: str = Field(..., exclude=True, alias="_id")
    name: str
    type: str
    plugins: list[PluginMeta] | None
    args: list[str] | None
    args_schema: str | None
    data_schema: str | None
    configs: list[Config] | None
    tasks: list["Task"] | None
    sub_tasks: list["Task"] | None
    description: str | None
    create_time: datetime
    update_time: datetime

    @computed_field
    def _id(self) -> str:
        return self.key
