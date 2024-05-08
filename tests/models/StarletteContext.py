from dataclasses import dataclass

from httpx import AsyncClient

from mercury.core.Context import Context


@dataclass
class StarletteContext:
    client: AsyncClient
    rds_auth: dict[str, str]
    context: Context
