class TripType:
    """Represents the type of a trip."""
    
    LOADED = "LOADED"
    EMPTY_DEADHEAD = "EMPTY_DEADHEAD"
    EMPTY_STRATEGIC = "EMPTY_STRATEGIC"
    
    VALID_TYPES = {LOADED, EMPTY_DEADHEAD, EMPTY_STRATEGIC}
    
    def __init__(self, trip_type: str):
        if trip_type not in self.VALID_TYPES:
            raise ValueError(f"Trip type must be one of {self.VALID_TYPES}")
        self.trip_type = trip_type
    
    def is_loaded(self) -> bool:
        """Check if trip is loaded with cargo."""
        return self.trip_type == self.LOADED
    
    def is_empty_deadhead(self) -> bool:
        """Check if trip is mandatory empty return."""
        return self.trip_type == self.EMPTY_DEADHEAD
    
    def is_empty_strategic(self) -> bool:
        """Check if trip is strategic empty return."""
        return self.trip_type == self.EMPTY_STRATEGIC
    
    def is_empty(self) -> bool:
        """Check if trip is any type of empty trip."""
        return self.trip_type in {self.EMPTY_DEADHEAD, self.EMPTY_STRATEGIC}
    
    def __eq__(self, other):
        if not isinstance(other, TripType):
            return False
        return self.trip_type == other.trip_type
    
    def __repr__(self):
        return f"TripType({self.trip_type})"

