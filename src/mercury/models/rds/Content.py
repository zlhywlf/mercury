from pydantic import BaseModel, Field


class Content(BaseModel):
    """"""
    params: list[dict] = Field(..., exclude=True)
    type: str = Field(..., exclude=True)
    code: int
    msg: str
    data: list["Content"] | dict[str, "Content"] | list[dict] | None
    sub_params: list[dict] | None = Field(..., exclude=True)
