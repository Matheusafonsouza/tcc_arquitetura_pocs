from fastapi.responses import JSONResponse

from ports.http import HTTPPort
from common.entities.user import User
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


def create_user(data: User):
    return UserRepository().create(data)


def delete_user(user_id: int):
    return UserRepository().delete(user_id)


def update_user(user_id: int, data: User):
    return UserRepository().update(user_id, data)
