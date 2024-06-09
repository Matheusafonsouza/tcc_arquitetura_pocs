import uvicorn
from fastapi import FastAPI

from common.service import ping, ping_server
from adapters.http import HTTPRequestAdapter
from common.amqp import get_rabbitmq_adapter


amqp_adapter = get_rabbitmq_adapter()


app = FastAPI()

@app.get("/ping")
def send_ping():
    return ping()


@app.get("/ping-server-2")
def ping_server_2():
    return ping_server(
        HTTPRequestAdapter,
        amqp_adapter,
        "http://server2:8000",
        "/ping",
    )


@app.get("/ping-server-3")
def ping_server_3():
    return ping_server(
        HTTPRequestAdapter,
        amqp_adapter,
        "http://server3:8000",
        "/ping",
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
