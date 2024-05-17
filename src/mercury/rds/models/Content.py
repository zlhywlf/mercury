from typing import Any

from pydantic import BaseModel, Field, computed_field


class Content(BaseModel):
    """"""

    param: dict[str, Any] = Field(..., exclude=True)
    task_type: str = Field(..., exclude=True)
    code: int
    msg: str
    data: list[Any] | dict[str, Any] | None

    @computed_field
    def type(self) -> str:
        return type(self.data).__name__

    @computed_field
    def total(self) -> int:
        return len(self.data) if isinstance(self.data, list) else 1
