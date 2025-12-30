from domain.value_objects.Revenue import Revenue
from domain.value_objects.Cost import Cost
from domain.value_objects.Profit import Profit
from domain.value_objects.TripType import TripType


class Trip:
    """Represents a single trip taken by a driver."""
    
    def __init__(self, trip_id: str, revenue: Revenue, cost: Cost, trip_type: TripType, 
                 wait_time: float = 0.0, bonus: float = 0.0):
        if not trip_id:
            raise ValueError("Trip ID cannot be empty")
        if not isinstance(revenue, Revenue):
            raise ValueError("Revenue must be a Revenue object")
        if not isinstance(cost, Cost):
            raise ValueError("Cost must be a Cost object")
        if not isinstance(trip_type, TripType):
            raise ValueError("Trip type must be a TripType object")
        if wait_time < 0:
            raise ValueError("Wait time cannot be negative")
        if bonus < 0:
            raise ValueError("Bonus cannot be negative")
        
        self.trip_id = trip_id
        self.revenue = revenue
        self.cost = cost
        self.trip_type = trip_type
        self.wait_time = wait_time
        self.bonus = bonus
    
    def calculate_profit(self) -> Profit:
        """Calculate profit for this trip: revenue - costs + bonuses."""
        return Profit(self.revenue, self.cost, self.bonus)
    
    def __repr__(self):
        return f"Trip(id='{self.trip_id}', type={self.trip_type.trip_type}, revenue={self.revenue.amount}, cost={self.cost.amount}, wait={self.wait_time}h)"

