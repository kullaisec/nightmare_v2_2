from flask import request
from middleware.cache_middleware import cache_response

@cache_response
def profile():
    return f"Hello {request.headers.get('X-User', 'guest')}"