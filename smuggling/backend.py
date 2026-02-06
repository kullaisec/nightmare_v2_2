from middleware.proxy_headers import get_real_content_length
from utils.request import parse_body

def backend_parse(raw):
    length = get_real_content_length()
    return parse_body(raw, length)