from fastapi import APIRouter
from controllers.auth_controller import register, login

router = APIRouter()


@router.post("/register")
def register_user(data: dict):

    if not register(data["username"], data["password"]):
        return {"error": "User exists"}

    return {"msg": "Registered"}


@router.post("/login")
def login_user(data: dict):

    token = login(data["username"], data["password"])

    if not token:
        return {"error": "Invalid credentials"}

    return {"token": token}
