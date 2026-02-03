from jose import jwt
from fastapi import HTTPException

SECRET = "MYSECRETKEY"


def verify(token):

    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except:
        raise HTTPException(401, "Invalid Token")
