from dataclasses import dataclass

from mercury.models.rds.Arg import Arg
from mercury.models.rds.TaskConfig import TaskConfig


@dataclass
class Task:
    _id: str
    type: str
    pre: str | None
    post: str | None
    args: list[Arg] | None
    configs: list[TaskConfig] | None
    sub_tasks: list["Task"] | None
