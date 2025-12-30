class Revenue:
    """Represents revenue from a trip."""
    
    def __init__(self, amount: float):
        if amount < 0:
            raise ValueError("Revenue cannot be negative")
        self.amount = amount
    
    def __eq__(self, other):
        if not isinstance(other, Revenue):
            return False
        return self.amount == other.amount
    
    def __repr__(self):
        return f"Revenue({self.amount})"

