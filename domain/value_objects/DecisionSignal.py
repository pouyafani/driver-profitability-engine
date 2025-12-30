class DecisionSignal:
    """Represents a profitability judgment: GREEN, YELLOW, or RED."""
    
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    RED = "RED"
    
    VALID_SIGNALS = {GREEN, YELLOW, RED}
    
    def __init__(self, signal: str):
        if signal not in self.VALID_SIGNALS:
            raise ValueError(f"Signal must be one of {self.VALID_SIGNALS}")
        self.signal = signal
    
    def is_green(self) -> bool:
        """Check if signal is GREEN."""
        return self.signal == self.GREEN
    
    def is_yellow(self) -> bool:
        """Check if signal is YELLOW."""
        return self.signal == self.YELLOW
    
    def is_red(self) -> bool:
        """Check if signal is RED."""
        return self.signal == self.RED
    
    def __eq__(self, other):
        if not isinstance(other, DecisionSignal):
            return False
        return self.signal == other.signal
    
    def __repr__(self):
        return f"DecisionSignal({self.signal})"

