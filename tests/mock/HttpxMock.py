from httpx import Request, Response


class HttpxMock:

    async def __call__(self, request: Request) -> Response:
        host = request.url.host
        path = request.url.path
        return Response(200, json={"text": "Hello, world!"})
