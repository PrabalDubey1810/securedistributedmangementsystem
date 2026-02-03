from passlib.hash import argon2
from src.config.db import users
from src.services.jwt_service import create_token


def clean_password(password: str):
    return str(password).strip()


def register(username, password):

    if not username or not password:
        return False, "Empty fields"

    password = clean_password(password)

    if users.find_one({"username": username}):
        return False, "User exists"

    # Hash using Argon2 (NO 72-byte limit)
    hashed = argon2.hash(password)

    users.insert_one({
        "username": username,
        "password": hashed
    })

    return True, "Registered"


def login(username, password):

    if not username or not password:
        return None

    password = clean_password(password)

    user = users.find_one({"username": username})

    if not user:
        return None

    if not argon2.verify(password, user["password"]):
        return None

    return create_token(username)
