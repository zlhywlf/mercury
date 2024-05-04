from httpx import AsyncClient

from mercury.core.clients.Http import Http


class HttpHttpx(Http):

    def __init__(self, *, client: AsyncClient):
        super().__init__()
        self.__client = client
