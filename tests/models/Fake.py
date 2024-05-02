from mercury.models.RdsApi import RdsApi
from mercury.models.RdsConfig import RdsConfig
from mercury.models.RdsData import RdsData

fake_config = [
    RdsConfig("table01", "app", [{"name": "a"}, {"name": "b"}], None, None, [
        RdsConfig("userInfo", "api", [{"name": "a"}, {"name": "b"}], None, None, None),
    ]),
]

fake_data = [
    RdsData("NO01", None, None, "data01", "a=1&b=2", "2020-01-01", "a=1&b=2", None),
    RdsData("NO02", "NO01", None, "data01", "a=1&b=2", "2020-01-02", "a=1&b=2&other=3", None),
    RdsData("NO03", None, None, "table01", "a=1&b=2", "2020-01-01", "a=1&b=2&other=3", [{}, {}]),
    RdsData("NO04", "NO03", "NO01", "table01", "a=1&b=2", "2020-01-01", "a=1&b=2", None),
]

fake_api = [
    RdsApi("userInfo", "http://localhost", "GET")
]
