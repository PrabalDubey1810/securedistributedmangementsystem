from passlib.hash import bcrypt
from config.db import users
from services.jwt_service import create_token


def register(username, password):

    if users.find_one({"username": username}):
        return False

    hashed = bcrypt.hash(password)

    users.insert_one({
        "username": username,
        "password": hashed
    })

    return True


def login(username, password):

    user = users.find_one({"username": username})

    if not user:
        return None

    if not bcrypt.verify(password, user["password"]):
        return None

    return create_token(username)
