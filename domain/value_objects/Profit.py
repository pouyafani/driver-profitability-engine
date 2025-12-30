from domain.value_objects.Revenue import Revenue
from domain.value_objects.Cost import Cost


class Profit:
    """Represents profit calculated as revenue - costs + bonuses."""
    
    def __init__(self, revenue: Revenue, cost: Cost, bonus: float = 0.0):
        if not isinstance(revenue, Revenue):
            raise ValueError("Revenue must be a Revenue object")
        if not isinstance(cost, Cost):
            raise ValueError("Cost must be a Cost object")
        if bonus < 0:
            raise ValueError("Bonus cannot be negative")
        
        self.amount = revenue.amount - cost.amount + bonus
        self.revenue = revenue
        self.cost = cost
        self.bonus = bonus
    
    def is_positive(self) -> bool:
        """Check if profit is positive."""
        return self.amount > 0
    
    def is_negative(self) -> bool:
        """Check if profit is negative."""
        return self.amount < 0
    
    def __eq__(self, other):
        if not isinstance(other, Profit):
            return False
        return self.amount == other.amount
    
    def __repr__(self):
        return f"Profit({self.amount})"

