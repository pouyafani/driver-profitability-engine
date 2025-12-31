class AuthenticatedPrincipal:
    def __init__(self, user_id: str, permissions: set[str]):
        self.user_id = user_id
        self.permissions = permissions

    @staticmethod
    def from_token(token: str) -> "AuthenticatedPrincipal":
        return AuthenticatedPrincipal(user_id="extracted", permissions=set())

