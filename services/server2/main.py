import uvicorn

from common.database import get_mongo_database
from common.repositories.user_repository import UserRepository
from fastapi import FastAPI, Body
from common import common_service
from common.common_service import ping, ping_server
from adapters.http import HTTPRequestAdapter
from common.amqp import get_rabbitmq_adapter

app = FastAPI()

amqp_adapter = get_rabbitmq_adapter()

user_repository = UserRepository(
    adapter=get_mongo_database("commonSchema", "users"))


@app.get("/ping")
def send_ping():
    return ping()


@app.get("/ping-server-1")
def ping_server_1():
    return ping_server(
        HTTPRequestAdapter,
        amqp_adapter,
        "http://server1:8000",
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


"""Uses a common database schema"""
@app.get("/users/{user_id}")
def get_user(user_id: str):
    return common_service.get_user(user_id, repository=user_repository)


@app.post("/users")
def create_user(payload: dict = Body(...)):
    return common_service.create_user(payload, repository=user_repository)


@app.put("/users/{user_id}")
def update_user(user_id: str, payload: dict = Body(...)):
    return common_service.update_user(user_id, payload, repository=user_repository)


@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    return common_service.delete_user(user_id, repository=user_repository)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
