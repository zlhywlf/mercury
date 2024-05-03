from mercury.models.rds.Arg import Arg
from mercury.models.rds.Task import Task
from mercury.models.rds.TaskConfig import TaskConfig

__user_info = Task(_id="userInfo", type="api", pre=None, post=None, args=[Arg(name="a"), Arg(name="b")],
                   configs=[TaskConfig(name="url", value="https://www.httpbin.org/get"),
                            TaskConfig(name="method", value="GET")],
                   sub_tasks=None)

fake_config = [
    __user_info,
    Task(_id="table01", type="app", pre=None, post=None, args=[Arg(name="a"), Arg(name="b")], configs=None,
         sub_tasks=[__user_info])
]
