from fastapi.responses import JSONResponse

from ports.http import HTTPPort


def ping():
    return { "ping": True }


def ping_server(
    HTTPAdapter: HTTPPort,
    server_url: str,
    route: str
):
    response = HTTPAdapter(server_url).get(route)
    return JSONResponse(
        status_code=response.get("status_code"),
        content=response.get("content"),
    )
