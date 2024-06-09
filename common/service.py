from ports.http import HTTPPort
from fastapi.responses import JSONResponse


def ping():
    return { "ping": True }


def ping_server(
    http_adapter: HTTPPort,
    server_url: str,
    route: str
):
    response = http_adapter(server_url).get(route)
    return JSONResponse(
        status_code=response.get("status_code"),
        content=response.get("content"),
    )
