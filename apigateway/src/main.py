import requests
from fastapi import FastAPI, Request

app = FastAPI()

AUTH_URL = "http://localhost:8001"
DATA_URL = "http://localhost:8002"


@app.post("/auth/{path}")
async def auth_proxy(path: str, req: Request):

    body = await req.json()

    res = requests.post(
        f"{AUTH_URL}/{path}",
        json=body
    )

    return res.json()


@app.get("/data")
def data_proxy(req: Request):

    token = req.headers.get("Authorization")

    res = requests.get(
        f"{DATA_URL}/data",
        headers={"Authorization": token}
    )

    return res.json()
