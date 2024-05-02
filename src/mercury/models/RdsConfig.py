from dataclasses import dataclass


@dataclass
class RdsConfig:
    _id: str
    type: str
    args: list[dict[str, str]]
    pre: str | None
    post: str | None
    objects: list["RdsConfig"] | None
