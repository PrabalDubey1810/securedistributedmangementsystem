from config.db import data_col


def get_private_data(username):

    data = data_col.find_one({"user": username})

    if not data:
        data_col.insert_one({
            "user": username,
            "info": "Welcome to private data"
        })

        return "Welcome to private data"

    return data["info"]
