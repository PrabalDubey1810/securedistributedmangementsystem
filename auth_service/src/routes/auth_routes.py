from fastapi import APIRouter
from src.controllers.auth_controller import register, login

router = APIRouter()


@router.post("/register")
def register_user(data: dict):

    ok, msg = register(data.get("username"), data.get("password"))

    if not ok:
        return {"error": msg}

    return {"msg": msg}


@router.post("/login")
def login_user(data: dict):

    token = login(data.get("username"), data.get("password"))

    if not token:
        return {"error": "Invalid credentials"}

    return {"token": token}
