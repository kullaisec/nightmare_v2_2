from flask import request

def get_real_content_length():

    if "Content-Length" in request.headers:
        try:
            return int(request.headers["Content-Length"])
        except ValueError:
            return None
    return None