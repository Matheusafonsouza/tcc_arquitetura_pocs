import uvicorn
from fastapi import FastAPI, Body

from domain import service
from common.service import ping, ping_server
from common.database import get_postgres_database
from adapters.http import HTTPRequestAdapter
from common.amqp import get_rabbitmq_adapter
from domain.repositories.user_repository import UserRepository


user_repository = UserRepository(
    adapter=get_postgres_database("users")
)

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


@app.get("/users/{user_id}")
def get_user(user_id: str):
    return service.get_user(user_id, repository=user_repository)


@app.post("/users")
def create_user(payload: dict = Body(...)):
    return service.create_user(payload, repository=user_repository)


@app.put("/users/{user_id}")
def update_user(user_id: str, payload: dict = Body(...)):
    return service.update_user(user_id, payload, repository=user_repository)


@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    return service.delete_user(user_id, repository=user_repository)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
