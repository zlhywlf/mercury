from pydantic import BaseModel

from mercury.rds.models.Config import Config


class PluginMeta(BaseModel):
    id: str
    configs: list[Config]
