from datetime import date, datetime

import orjson
from pydantic import BaseModel

from mercury.models.rds.Config import Config
from mercury.models.rds.PluginMeta import PluginMeta
from mercury.models.rds.Task import Task


class SimpleTaskSimpleArg(BaseModel):
    arg: str


class SimpleTaskItem(BaseModel):
    a: str | None
    b: int | None
    c: float | None
    d: list | None
    e: dict | None
    f: date | None


class SimpleTaskData(BaseModel):
    items: list[SimpleTaskItem]
    num: int
    total: int


class SimpleTaskResponse(BaseModel):
    code: int
    data: SimpleTaskData | None
    msg: str | None


exp = ("[].data.items[].{" "str: a," "int: b," "float: c," "list: d," "dict: e," "date: f,").strip(",") + "}"

simple_task = Task(
    _id="simple_task",
    name="simple",
    type="api",
    plugins=[PluginMeta(id="data_parsing", configs=[Config(name="expression", value=exp)])],
    args=["arg"],
    args_schema=orjson.dumps(SimpleTaskSimpleArg.model_json_schema()),
    data_schema=orjson.dumps(SimpleTaskResponse.model_json_schema()),
    configs=[
        Config(name="host", value="http://mocks.fakes.tasks"),  # 当前模块路径
        Config(name="path", value="/SimpleTask"),  # 当前模块名称
        Config(name="method", value="POST"),
    ],
    sub_tasks=None,
    description="description",
    create_time=datetime.now(),
    update_time=datetime.now(),
)


def handle(arg: str, **kwargs) -> SimpleTaskResponse:
    """mock数据获取入口"""
    return orjson.loads(globals().get(arg))


simple_task_response_200 = SimpleTaskResponse(
    code=200,
    msg="",
    data=SimpleTaskData(num=1, total=1, items=[SimpleTaskItem(a="string", b=100, c=1.1, d=[], e={}, f=date.today())]),
).model_dump_json()
