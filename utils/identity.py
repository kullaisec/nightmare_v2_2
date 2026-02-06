from flask import request

def get_identity():

    return {
        "user": request.headers.get("X-User"),
        "role": request.headers.get("X-Role"),
        "auth": request.headers.get("Authorization")
    }