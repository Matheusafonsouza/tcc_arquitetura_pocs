from fastapi.responses import JSONResponse

from ports.http import HTTPPort
from domain.repositories.user_repository import UserRepository


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

def get_user(user_id: int):
    return UserRepository().get(user_id)
