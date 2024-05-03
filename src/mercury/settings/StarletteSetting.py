from typing import override

from starlette.config import Config

from mercury.core.Setting import Setting


class StarletteSetting(Setting):

    def __init__(self, env_name=".env"):
        self._config = Config(env_name)

    @property
    @override
    def is_debug(self) -> bool:
        return self._config("DEBUG", cast=bool, default=False)

    @property
    @override
    def rds_key(self) -> str:
        return self._config("RDS_KEY", cast=str, default="key")

    @property
    @override
    def mongo(self) -> str:
        return self._config("MONGO", cast=str, default="mongodb://localhost:27017")

    @property
    @override
    def rds_task_table_name(self) -> str:
        """"""
        return self._config("RDS_TASK_TABLE_NAME", cast=str, default="rds_task")

    @property
    @override
    def rds_data_table_name(self) -> str:
        """"""
        return self._config("RDS_DATA_TABLE_NAME", cast=str, default="rds_data")
