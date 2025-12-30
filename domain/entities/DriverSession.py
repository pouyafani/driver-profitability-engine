from domain.entities.Trip import Trip
from domain.value_objects.Profit import Profit
from domain.value_objects.DecisionSignal import DecisionSignal
from domain.value_objects.TripType import TripType


class DriverSession:
    """Represents a time-bounded context for profitability decisions."""
    
    def __init__(self, session_id: str, driver_id: str):
        if not session_id:
            raise ValueError("Session ID cannot be empty")
        if not driver_id:
            raise ValueError("Driver ID cannot be empty")
        
        self.session_id = session_id
        self.driver_id = driver_id
        self.trips = []
    
    def add_trip(self, trip: Trip):
        """Add a trip to this session."""
        if not isinstance(trip, Trip):
            raise ValueError("Trip must be a Trip object")
        self.trips.append(trip)
    
    def calculate_total_profit(self) -> float:
        """Calculate total profit for all trips in this session."""
        total = 0.0
        for trip in self.trips:
            profit = trip.calculate_profit()
            total += profit.amount
        return total
    
    def calculate_total_wait_time(self) -> float:
        """Calculate total wait time across all trips."""
        return sum(trip.wait_time for trip in self.trips)
    
    def count_empty_trips(self) -> int:
        """Count the number of empty trips (deadhead or strategic)."""
        return sum(1 for trip in self.trips if trip.trip_type.is_empty())
    
    def determine_signal(self, green_threshold: float = 50.0, yellow_threshold: float = 0.0,
                        max_wait_hours: float = 8.0, max_empty_ratio: float = 0.5) -> DecisionSignal:
        """Determine decision signal using simple, explainable rules.
        
        Rules:
        1. Base signal from total profit (revenue - costs + bonuses)
        2. Adjust down if too many empty trips (risk factor)
        3. Adjust down if excessive wait time (risk factor)
        """
        total_profit = self.calculate_total_profit()
        total_wait = self.calculate_total_wait_time()
        empty_count = self.count_empty_trips()
        total_trips = len(self.trips)
        
        # Start with base profit signal
        if total_profit >= green_threshold:
            base_signal = DecisionSignal.GREEN
        elif total_profit >= yellow_threshold:
            base_signal = DecisionSignal.YELLOW
        else:
            base_signal = DecisionSignal.RED
        
        # Adjust for empty trips (risk factor)
        if total_trips > 0:
            empty_ratio = empty_count / total_trips
            if empty_ratio > max_empty_ratio:
                # Too many empty trips - downgrade signal
                if base_signal == DecisionSignal.GREEN:
                    base_signal = DecisionSignal.YELLOW
                elif base_signal == DecisionSignal.YELLOW:
                    base_signal = DecisionSignal.RED
        
        # Adjust for wait time (risk factor)
        if total_wait > max_wait_hours:
            # Excessive wait time - downgrade signal
            if base_signal == DecisionSignal.GREEN:
                base_signal = DecisionSignal.YELLOW
            elif base_signal == DecisionSignal.YELLOW:
                base_signal = DecisionSignal.RED
        
        return DecisionSignal(base_signal)
    
    def __repr__(self):
        return f"DriverSession(id='{self.session_id}', driver_id='{self.driver_id}', trips={len(self.trips)})"

