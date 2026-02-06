CACHE = {}

def get(key):
    return CACHE.get(key)

def set(key, value, meta=None):
    CACHE[key] = (value, meta)