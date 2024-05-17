from datetime import date, datetime

import orjson
from mercury.rds.models.Config import Config
from mercury.rds.models.PluginMeta import PluginMeta
from mercury.rds.models.Task import Task
from pydantic import BaseModel

from tests.mocks.tasks.SimpleApi import simple_api


class SimpleTableArg(BaseModel):
    arg: str


class JsonData(BaseModel):
    a: int


class SimpleTableItem(BaseModel):
    json_data: list[JsonData] | None
    g: str | None
    str: str | None
    int: int | None
    float: float | None
    list: list | None
    dict: dict | None
    date: date | None


class SimpleTableSchema(BaseModel):
    code: int
    msg: str | None
    data: list[SimpleTableItem] | None


exp = (
    "[].data.items[].{"
    "str: a,"
    "int: convert_unit(b,a),"
    "float: c,"
    "list: d,"
    "dict: e,"
    "g: g,"
    "json_data: to_json(js),"
    "date: f}"
)

simple_table_sub = Task(
    _id="simple_table_sub",
    name="table_sub",
    type="subject",
    plugins=[
        PluginMeta(id="default_param", configs=[Config(name="size", value=10)]),
        PluginMeta(
            id="param_map",
            configs=[
                Config(name="int", value="index"),
                Config(name="g", value="name"),
                Config(name="str", value="arg"),
            ],
        ),
    ],
    args=["arg"],
    args_schema=orjson.dumps(SimpleTableItem.model_json_schema()),
    data_schema=None,
    configs=None,
    tasks=[simple_api],
    sub_tasks=None,
    description="description",
    create_time=datetime.now(),
    update_time=datetime.now(),
)

simple_table = Task(
    _id="simple_table",
    name="table",
    type="table",
    plugins=[
        PluginMeta(id="data_parsing", configs=[Config(name="expression", value=exp)]),
        PluginMeta(
            id="default_param",
            configs=[Config(name="index", value=1), Config(name="size", value=10)],
        ),
    ],
    args=["arg"],
    args_schema=orjson.dumps(SimpleTableArg.model_json_schema()),
    data_schema=orjson.dumps(SimpleTableSchema.model_json_schema()),
    configs=None,
    tasks=[simple_api],
    sub_tasks=[simple_table_sub],
    description="description",
    create_time=datetime.now(),
    update_time=datetime.now(),
)
