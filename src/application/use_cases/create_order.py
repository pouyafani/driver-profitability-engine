from src.application.security.authorization import authorize

def create_order(command, principal):
    authorize(principal, "create_order", "order")
    return True

