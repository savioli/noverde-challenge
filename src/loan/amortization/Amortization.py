from abc import ABC, abstractmethod


class Amortization(ABC):
    """A base class for an amortization method"""

    @abstractmethod
    def configure(self, interest_rate, present_value, time_in_months, precision):
        """Configures the parameters for an amortization method"""
        pass
