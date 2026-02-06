STATES = {}

def save(state, ip):
    STATES[state] = ip

def valid(state, ip):
    return STATES.get(state) == ip