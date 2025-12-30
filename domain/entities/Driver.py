class Driver:
    """Represents a driver in the system."""
    
    def __init__(self, driver_id: str, name: str = ""):
        if not driver_id:
            raise ValueError("Driver ID cannot be empty")
        
        self.driver_id = driver_id
        self.name = name
    
    def __repr__(self):
        return f"Driver(id='{self.driver_id}', name='{self.name}')"

