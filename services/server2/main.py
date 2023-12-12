import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from adapters.http import HTTPRequestAdapter

app = FastAPI()


@app.get("/ping")
def ping():
    return { "ping": True }


@app.get("/ping-server-1")
def ping_server_1():
    response = HTTPRequestAdapter("http://server1:8000").get("/ping")
    return JSONResponse(
        status_code=response.get("status_code"),
        content=response.get("content"),
    )


@app.get("/ping-server-3")
def ping_server_3():
    response = HTTPRequestAdapter("http://server3:8000").get("/ping")
    return JSONResponse(
        status_code=response.get("status_code"),
        content=response.get("content"),
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
