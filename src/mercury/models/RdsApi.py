from dataclasses import dataclass


@dataclass
class RdsApi:
    _id: str
    url: str
    method: str
