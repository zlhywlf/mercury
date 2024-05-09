from importlib import import_module

import orjson
from httpx import Request, Response


class HttpxMock:

    async def __call__(self, request: Request) -> Response:
        host = request.url.host
        path = request.url.path
        content = orjson.loads(request.content.decode("utf-8") or "{}")
        params = {**request.url.params, **content}
        module_name = host + path.replace("/", ".")
        m = import_module(module_name, ".")
        data = getattr(m, "handle")(**params)
        return Response(200, json=data)
