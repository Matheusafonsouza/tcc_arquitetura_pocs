from ports.http import HTTPPort
from ports.amqp import AMQPPort
from fastapi.responses import JSONResponse
from common.entities.user import User
from ports.database import DatabasePort


def ping():
    return { "ping": True }


def ping_server(
    http_adapter: HTTPPort,
    amqp_adapter: AMQPPort,
    server_url: str,
    route: str
):
    response = http_adapter(server_url).get(route)
    amqp_adapter.send_message(response)
    return JSONResponse(
        status_code=response.get("status_code"),
        content=response.get("content"),
    )

def get_user(user_id: str, repository: DatabasePort):
    return repository.get(user_id)

def create_user(data: User, repository: DatabasePort):
    return repository.create(data)

def delete_user(user_id: str, repository: DatabasePort):
    return repository.delete(user_id)

def update_user(user_id: str, data: User, repository: DatabasePort):
    return repository.update(user_id, data)
