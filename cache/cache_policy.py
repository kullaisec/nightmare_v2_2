def is_cacheable(response, meta):
    return meta.get("authenticated") is True