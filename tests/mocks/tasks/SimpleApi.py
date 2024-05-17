from datetime import date, datetime

import orjson
from mercury.rds.models.Config import Config
from mercury.rds.models.PluginMeta import PluginMeta
from mercury.rds.models.Task import Task
from pydantic import BaseModel


class SimpleApiArg(BaseModel):
    arg: str
    index: int
    size: int


class SimpleApiItem(BaseModel):
    a: str | None
    b: int | None
    c: float | None
    d: list | None
    e: dict | None
    f: date | None
    js: str | None
    g: str | None


class SimpleApiData(BaseModel):
    items: list[SimpleApiItem]
    num: int
    total: int


class SimpleApiResponse(BaseModel):
    code: int
    data: SimpleApiData | None
    msg: str | None


class SimpleApiSchema(BaseModel):
    code: int
    msg: str | None
    data: SimpleApiResponse | None


simple_api = Task(
    _id="simple_api",
    name="api",
    type="api",
    plugins=[
        PluginMeta(
            id="dynamic_api",
            configs=[
                Config(name="total_expression", value="data.total"),
                Config(name="size_expression", value="data.num"),
            ],
        ),
        PluginMeta(
            id="param_map",
            configs=[
                Config(name="page_number", value="index"),
                Config(name="page_size", value="size"),
            ],
        ),
    ],
    args=["arg", "index", "size"],
    args_schema=orjson.dumps(SimpleApiArg.model_json_schema()),
    data_schema=orjson.dumps(SimpleApiSchema.model_json_schema()),
    configs=[
        Config(name="host", value="http://mocks.tasks"),  # 当前模块路径
        Config(name="path", value="/SimpleApi"),  # 当前模块名称
        Config(name="method", value="POST"),
    ],
    tasks=None,
    sub_tasks=None,
    description="description",
    create_time=datetime.now(),
    update_time=datetime.now(),
)


def handle(arg: str, index: int, size: int, **kwargs) -> SimpleApiResponse:
    """mock数据获取入口"""
    if arg != "simple_api_response_200":
        return orjson.loads(globals().get("simple_api_response_200_1_10"))
    return orjson.loads(globals().get(f"{arg}_{index}_{size}"))


items = [
    SimpleApiItem(
        a="万元" if _ % 2 == 0 else "元",
        b=_,
        c=1.1,
        d=[],
        e={},
        f=date.today(),
        js=f'[{{"a":{_}}}]',
        g=f"g{_}",
    )
    for _ in range(20)
]

simple_api_response_200_1_10 = SimpleApiResponse(
    code=200,
    msg="",
    data=SimpleApiData(num=10, total=20, items=items[0:10]),
).model_dump_json()

simple_api_response_200_2_10 = SimpleApiResponse(
    code=200,
    msg="",
    data=SimpleApiData(num=10, total=20, items=items[10:20]),
).model_dump_json()
