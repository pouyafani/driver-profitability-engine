class PolicyRegistry:
    @staticmethod
    def is_allowed(principal, action, resource, context=None) -> bool:
        return action in principal.permissions

