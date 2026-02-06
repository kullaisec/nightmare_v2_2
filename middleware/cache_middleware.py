from flask import request
from cache.cache_store import get, set
from cache.cache_policy import is_cacheable

def cache_response(handler):
    def wrapper(*args, **kwargs):
        key = request.path

        cached = get(key)
        if cached:
            return cached[0]

        response = handler(*args, **kwargs)
        meta = {
            "authenticated": request.headers.get("Authorization") is not None
        }

        if is_cacheable(response, meta):
            set(key, response, meta)

        return response
    return wrapper