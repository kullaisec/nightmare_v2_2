from flask import request
from oauth.state_store import valid
from oauth.token_cache import store

def oauth_callback():
    state = request.args.get("state")
    code = request.args.get("code")
    ip = request.headers.get("X-Forwarded-For")

    if not valid(state, ip):
        return "Invalid state", 400

    store(code, request.headers.get("X-User"))
    return "Logged in"