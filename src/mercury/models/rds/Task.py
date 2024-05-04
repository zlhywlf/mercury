from pydantic import BaseModel, Field, computed_field

from mercury.models.rds.Config import Config


class Task(BaseModel):
    key: str = Field(..., exclude=True, alias="_id")
    type: str
    pre: str | None
    post: str | None
    args: list[str] | None
    args_schema: dict | None
    configs: list[Config] | None
    sub_tasks: list["Task"] | None

    @computed_field
    @property
    def _id(self) -> str:
        return self.key
