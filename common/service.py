from ports.http import HTTPPort
from ports.amqp import AMQPPort
from fastapi.responses import JSONResponse


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
