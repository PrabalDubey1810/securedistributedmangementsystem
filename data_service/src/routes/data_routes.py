from fastapi import APIRouter, Header
from middlewares.jwt_middleware import verify
from controllers.data_controller import get_private_data

router = APIRouter()


@router.get("/data")
def private_data(authorization: str = Header()):

    token = authorization.replace("Bearer ", "")

    payload = verify(token)

    return {
        "data": get_private_data(payload["sub"])
    }
