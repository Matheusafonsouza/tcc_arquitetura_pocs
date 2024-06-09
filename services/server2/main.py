import uvicorn
from fastapi import FastAPI

from common.service import ping, ping_server
from adapters.http import HTTPRequestAdapter

app = FastAPI()


@app.get("/ping")
def ping():
    return ping()


@app.get("/ping-server-1")
def ping_server_1():
    return ping_server(
        HTTPRequestAdapter,
        "http://server1:8000",
        "/ping",
    )


@app.get("/ping-server-3")
def ping_server_3():
    return ping_server(
        HTTPRequestAdapter,
        "http://server3:8000",
        "/ping",
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
