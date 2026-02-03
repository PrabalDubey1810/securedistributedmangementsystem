from fastapi import FastAPI
from src.routes.data_routes import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def home():
    return {"service": "Data Service"}
