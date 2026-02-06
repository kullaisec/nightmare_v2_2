from flask import request

def get_user():
    return request.headers.get("X-User")

def get_role():
    return request.headers.get("X-Role", "user")

def is_admin():
    return get_role() == "admin"