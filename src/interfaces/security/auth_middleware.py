from src.application.security.principal import AuthenticatedPrincipal

def authenticate(request) -> AuthenticatedPrincipal:
    token = request.headers.get("Authorization")
    if not token:
        raise PermissionError("Missing token")
    return AuthenticatedPrincipal.from_token(token)

