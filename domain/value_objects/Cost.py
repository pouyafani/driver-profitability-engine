class Cost:
    """Represents cost for a trip."""
    
    def __init__(self, amount: float):
        if amount < 0:
            raise ValueError("Cost cannot be negative")
        self.amount = amount
    
    def __eq__(self, other):
        if not isinstance(other, Cost):
            return False
        return self.amount == other.amount
    
    def __repr__(self):
        return f"Cost({self.amount})"

