from typing import Any

from pydantic import BaseModel, Field, computed_field


class Data(BaseModel):
    key: str = Field(..., exclude=True, alias="_id")
    actual_id: str | None
    parent_id: str | None
    config_id: str
    create_date: str
    args: str
    data: list[Any] | None

    @computed_field  # type: ignore[misc]
    @property
    def _id(self) -> str:
        return self.key
