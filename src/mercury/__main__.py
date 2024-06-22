"""Application launcher.

Copyright (c) 2023-present 善假于PC也 (zlhywlf) .
"""

import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


def main() -> None:
    """Launcher."""
    uvicorn.run(
        Starlette(
            debug=True,
            routes=[
                Route("/", lambda request: JSONResponse({"hello": "mercury"}))  # noqa: ARG005
            ],
        )
    )  # pragma: no cover


if __name__ == "__main__":
    main()
