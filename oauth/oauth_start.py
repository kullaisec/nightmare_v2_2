from flask import request, redirect
from oauth.state_store import save

def oauth_start():
    state = request.args.get("state")
    ip = request.headers.get("X-Forwarded-For")

    save(state, ip)

    return redirect(
        f"https://idp.example/auth?state={state}"
    )