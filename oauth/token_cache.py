TOKENS = {}

def store(token, user):
    TOKENS[token] = user

def get(token):
    return TOKENS.get(token)