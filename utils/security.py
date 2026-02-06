from flask import request

def is_internal_request():

    ip = request.headers.get("X-Forwarded-For", "127.0.0.1")
    return ip.startswith("127.")