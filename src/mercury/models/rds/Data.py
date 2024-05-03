from dataclasses import dataclass


@dataclass
class Data:
    _id: str
    actual_id: str | None
    parent_id: str | None
    config_id: str
    key: str
    create_date: str
    args: str
    data: list | None
