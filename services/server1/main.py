import uvicorn
from fastapi import FastAPI

from domain import service
from adapters.http import HTTPRequestAdapter

app = FastAPI()


@app.get("/ping")
def ping():
    return service.ping()


@app.get("/ping-server-2")
def ping_server_2():
    return service.ping_server(
        HTTPRequestAdapter,
        "http://server2:8000",
        "/ping",
    )


@app.get("/ping-server-3")
def ping_server_3():
    return service.ping_server(
        HTTPRequestAdapter,
        "http://server3:8000",
        "/ping",
    )

@app.get("/users/{user_id}")
def ping_server_3(user_id: int):
    return service.get_user(user_id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
