from abc import ABC, abstractmethod


class CreditPolicy(ABC):
    """A base class for a policy"""

    @abstractmethod
    def evaluate(self, loan_request):
        """The logic of the policy to be evaluated"""
        pass
