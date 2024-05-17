from dataclasses import dataclass

from httpx import AsyncClient
from mercury.core.Context import Context


@dataclass
class TestContext:
    client: AsyncClient
    auth: dict[str, str]
    context: Context
