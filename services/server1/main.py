import uvicorn
from fastapi import FastAPI, Body

from common import common_service
from common.common_service import ping, ping_server
from common.database import get_postgres_database, get_mongo_database
from adapters.http import HTTPRequestAdapter
from common.amqp import get_rabbitmq_adapter

# Repositories
from common.repositories.user_repository import UserRepository
from domain.repositories.book_repository import BookRepository


user_repository = UserRepository(
    adapter=get_postgres_database( "commonSchema", "users")
)

book_repository = BookRepository(
    adapter=get_postgres_database("serviceOneSchema", "books")
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
@app.get("/books/{book_id}")
def get_book(book_id: str):
    return book_repository.get(book_id)


@app.post("/books")
def create_book(payload: dict = Body(...)):
    return book_repository.create(payload)


@app.put("/books/{book_id}")
def update_book(book_id: str, payload: dict = Body(...)):
    return book_repository.update(book_id, payload)


@app.delete("/books/{book_id}")
def delete_book(book_id: str):
    return book_repository.delete(book_id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
