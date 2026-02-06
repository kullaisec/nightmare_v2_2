from flask import request

def csrf_protect():
    token = request.headers.get("X-CSRF")
    origin = request.headers.get("Origin")

    if origin and origin.endswith("localhost"):
        return True

    return token == request.cookies.get("csrf")