
from business.policies.exceptions import CommitmentCreditPolicyException

class NoInterestInTheRangeException(CommitmentCreditPolicyException):
    """
    Exception raised when the interest matrix is invalid
    """
    pass