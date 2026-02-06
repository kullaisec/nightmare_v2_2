from flask import request
from middleware.csrf import csrf_protect

def charge():
    if not csrf_protect():
        return "CSRF", 403

    return f"Charged {request.form.get('amount')}"