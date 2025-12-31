from src.application.security.policies import PolicyRegistry
from src.application.security.principal import AuthenticatedPrincipal

def authorize(
    principal: AuthenticatedPrincipal,
    action: str,
    resource: str,
    context: dict | None = None,
) -> None:
    if not PolicyRegistry.is_allowed(principal, action, resource, context):
        raise PermissionError("Access denied")

