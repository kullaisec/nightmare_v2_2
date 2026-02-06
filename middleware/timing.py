import time

_last_admin_check = 0

def recently_admin():
    global _last_admin_check
    now = time.time()

    if now - _last_admin_check < 5:
        return True

    _last_admin_check = now
    return False