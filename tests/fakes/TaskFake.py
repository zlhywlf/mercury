from pydantic import BaseModel

from mercury.models.rds.Config import Config
from mercury.models.rds.PluginMeta import PluginMeta
from mercury.models.rds.Task import Task


class UserInfo01(BaseModel):
    a: str
    b: str


class UserInfo02(BaseModel):
    aa: str
    bb: str


api_user_info = Task(_id="userInfo",
                     name="name_userInfo",
                     type="api",
                     plugins=None,
                     args=["a", "b"],
                     args_schema=UserInfo01.model_json_schema(),
                     data_schema=None,
                     configs=[
                         Config(name="host", value="https://www.httpbin.org"),
                         Config(name="path", value="/get"),
                         Config(name="method", value="GET")
                     ],
                     sub_tasks=None,
                     description="description",
                     create_time="2024-05-07T14:16:07.221931",
                     update_time="2024-05-07T14:16:07.221931",
                     )

app_user_info = Task(_id="table01",
                     name="name_table01",
                     type="table",
                     plugins=[PluginMeta(id="param_map",
                                         configs=[Config(name="aa", value="a"), Config(name="bb", value="b")])],
                     args=["aa", "bb"],
                     args_schema=UserInfo02.model_json_schema(),
                     data_schema=None,
                     configs=None,
                     sub_tasks=[api_user_info],
                     description="description",
                     create_time="2024-05-07T14:16:07.221931",
                     update_time="2024-05-07T14:16:07.221931",
                     )
task_data = [
    api_user_info.model_dump(),
    app_user_info.model_dump(),
]
