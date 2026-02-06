from middleware.cache_middleware import cache_response
from middleware.auth_context import is_admin
from middleware.timing import recently_admin

@cache_response
def admin():
    if not (is_admin() or recently_admin()):
        return "Forbidden", 403
    return "ADMIN DATA"