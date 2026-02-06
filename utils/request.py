def parse_body(raw, length):

    if length is None:
        return raw
    return raw[:length]