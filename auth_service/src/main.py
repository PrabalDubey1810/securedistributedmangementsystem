from fastapi import FastAPI
from src.routes.auth_routes import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def home():
    return {"service": "Auth Service"}
