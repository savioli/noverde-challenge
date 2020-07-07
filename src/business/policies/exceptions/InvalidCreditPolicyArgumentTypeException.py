
from business.policies.exceptions import CreditPolicyException

class InvalidCreditPolicyArgumentTypeException(CreditPolicyException):
    """
    Exception raised when the argument is not from the correct type
    """
    pass