import requests
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, JSONResponse

app = FastAPI()

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

AUTH_URL = "http://localhost:8001"
DATA_URL = "http://localhost:8002"


@app.post("/auth/{path}")
async def auth_proxy(path: str, req: Request):

    body = await req.json()

    res = requests.post(
        f"{AUTH_URL}/{path}",
        json=body
    )
    # If the auth service returned JSON, forward it; otherwise forward raw content
    content_type = res.headers.get("content-type", "")
    try:
        if "application/json" in content_type:
            return JSONResponse(status_code=res.status_code, content=res.json())
        return Response(content=res.content, status_code=res.status_code, media_type=content_type or "text/plain")
    except ValueError:
        # failed to decode JSON; return raw content instead
        return Response(content=res.content, status_code=res.status_code, media_type=content_type or "text/plain")


@app.get("/data")
def data_proxy(req: Request):

    token = req.headers.get("Authorization")

    res = requests.get(
        f"{DATA_URL}/data",
        headers={"Authorization": token}
    )

    content_type = res.headers.get("content-type", "")
    try:
        if "application/json" in content_type:
            return JSONResponse(status_code=res.status_code, content=res.json())
        return Response(content=res.content, status_code=res.status_code, media_type=content_type or "text/plain")
    except ValueError:
        return Response(content=res.content, status_code=res.status_code, media_type=content_type or "text/plain")
