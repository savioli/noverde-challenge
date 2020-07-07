
from business.policies.exceptions import CreditPolicyException

class MandatoryCreditPolicyArgumentNotFoundException(CreditPolicyException):
    """
    Exception raised when a mandatory argument for a policy
    is not passed
    """
    pass