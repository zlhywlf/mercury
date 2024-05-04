from pydantic import BaseModel

from mercury.models.rds.Task import Task
from mercury.models.rds.TaskConfig import TaskConfig


class UserInfo(BaseModel):
    a: str
    b: str


__user_info = Task(_id="userInfo",
                   type="api",
                   pre=None,
                   post=None,
                   args=["a", "b"],
                   args_schema=UserInfo.model_json_schema(),
                   configs=[TaskConfig(name="url", value="https://www.httpbin.org/get"),
                            TaskConfig(name="method", value="GET")],
                   sub_tasks=None)

fake_config = [
    __user_info,
    Task(_id="table01",
         type="app",
         pre=None,
         post=None,
         args=["a", "b"],
         args_schema=UserInfo.model_json_schema(),
         configs=None,
         sub_tasks=[__user_info])
]
