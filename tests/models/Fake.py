from pydantic import BaseModel

from mercury.models.rds.Config import Config
from mercury.models.rds.Task import Task


class UserInfo(BaseModel):
    a: str
    b: str


api_user_info = Task(_id="userInfo",
                     type="api",
                     pre=None,
                     post=None,
                     args=["a", "b"],
                     args_schema=UserInfo.model_json_schema(),
                     configs=[Config(name="url", value="https://www.httpbin.org/get"),
                              Config(name="method", value="GET")],
                     sub_tasks=None)

app_user_info = Task(_id="table01",
                     type="app",
                     pre=None,
                     post=None,
                     args=["a", "b"],
                     args_schema=UserInfo.model_json_schema(),
                     configs=None,
                     sub_tasks=[api_user_info])

fake_config = [
    api_user_info,
    app_user_info
]
