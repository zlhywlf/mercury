from pydantic import BaseModel

from mercury.models.rds.Config import Config


class PluginMeta(BaseModel):
    id: str
    configs: list[Config]
