from datetime import datetime
from typing import Any

import orjson
from mercury.rds.models.Config import Config
from mercury.rds.models.PluginMeta import PluginMeta
from mercury.rds.models.Task import Task
from pydantic import BaseModel

from tests.mocks.tasks.SimpleApi import simple_api
from tests.mocks.tasks.SimpleTable import simple_table


class SimpleSubjectArg(BaseModel):
    subject_arg: str


class SimpleSubjectSchema(BaseModel):
    code: int
    msg: str | None
    data: dict[str, Any] | None


simple_subject01 = Task(
    _id="simple_subject01",
    name="subject01",
    type="subject",
    plugins=[
        PluginMeta(id="param_map", configs=[Config(name="subject01", value="name")]),
    ],
    args=["subject01", "arg"],
    args_schema=None,
    data_schema=None,
    configs=None,
    tasks=[simple_table],
    sub_tasks=None,
    description="description",
    create_time=datetime.now(),
    update_time=datetime.now(),
)

simple_subject02 = Task(
    _id="simple_subject02",
    name="subject02",
    type="subject",
    plugins=[
        PluginMeta(
            id="default_param",
            configs=[Config(name="index", value=1), Config(name="size", value=10)],
        ),
        PluginMeta(id="param_map", configs=[Config(name="subject02", value="name")]),
    ],
    args=["subject02", "arg"],
    args_schema=None,
    data_schema=None,
    configs=None,
    tasks=[simple_table, simple_api],
    sub_tasks=None,
    description="description",
    create_time=datetime.now(),
    update_time=datetime.now(),
)

simple_subject = Task(
    _id="simple_subject",
    name="subject",
    type="subject",
    plugins=[
        PluginMeta(id="param_map", configs=[Config(name="subject_arg", value="arg")]),
    ],
    args=["subject_arg"],
    args_schema=orjson.dumps(SimpleSubjectArg.model_json_schema()),
    data_schema=orjson.dumps(SimpleSubjectSchema.model_json_schema()),
    configs=None,
    tasks=[simple_subject01, simple_subject02],
    sub_tasks=None,
    description="description",
    create_time=datetime.now(),
    update_time=datetime.now(),
)
