from fastapi.responses import JSONResponse

from ports.http import HTTPPort
from adapters.rabbitmq import RabbitMQAMQPAdapter


def ping():
    return { "ping": True }


def ping_server(
    http_adapter: HTTPPort,
    server_url: str,
    route: str
):
    response = http_adapter(server_url).get(route)
    RabbitMQAMQPAdapter(
        host="rabbitmq",
        port=5672,
        username="test",
        password="test",
        virtual_host="/",
        topic="test",
    ).send_message(response)
    return JSONResponse(
        status_code=response.get("status_code"),
        content=response.get("content"),
    )
