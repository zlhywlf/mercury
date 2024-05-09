from pydantic import BaseModel, Field


class Content(BaseModel):
    """"""

    param: dict = Field(..., exclude=True)
    type: str = Field(..., exclude=True)
    code: int
    msg: str
    data: list["Content"] | dict[str, "Content"] | list[dict] | None
    sub_param: dict | None = Field(..., exclude=True)
