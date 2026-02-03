from jose import jwt
from datetime import datetime, timedelta

SECRET = "MYSECRETKEY"
ALGO = "HS256"


def create_token(username):

    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=2)
    }

    return jwt.encode(payload, SECRET, algorithm=ALGO)


def verify_token(token):

    return jwt.decode(token, SECRET, algorithms=[ALGO])
