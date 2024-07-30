import uvicorn
from fastapi import FastAPI

from common.database import get_mongo_database, get_postgres_database
from common.repositories.user_repository import UserRepository
from domain.repositories.tv_show_repository import TvShowRepository
from fastapi import FastAPI, Body
from common import common_service
from common.common_service import ping, ping_server

from adapters.http import HTTPRequestAdapter
from common.amqp import get_rabbitmq_adapter


app = FastAPI()

amqp_adapter = get_rabbitmq_adapter()

user_repository = UserRepository(
    adapter=get_postgres_database("commonSchema", "users"))

tv_show_repository = TvShowRepository(
    adapter=get_postgres_database("serviceThreeSchema", "tv_shows"))

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

"""Uses a isolated database schema"""
@app.get("/tv-shows/{tv_show_id}")
def get_tv_show(tv_show_id: str):
    return tv_show_repository.get(tv_show_id)


@app.post("/tv-shows")
def create_tv_show(payload: dict = Body(...)):
    return tv_show_repository.create(payload)


@app.put("/tv-shows/{tv_show_id}")
def update_tv_show(tv_show_id: str, payload: dict = Body(...)):
    return tv_show_repository.update(tv_show_id, payload)


@app.delete("/tv-shows/{tv_show_id}")
def delete_tv_show(tv_show_id: str):
    return tv_show_repository.delete(tv_show_id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
