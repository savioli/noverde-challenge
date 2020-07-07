
from business.policies.exceptions import CommitmentCreditPolicyException

class InvalidCommitmentCreditPolicyInterestMatrixException(CommitmentCreditPolicyException):
    """
    Exception raised when the interest matrix is invalid
    """
    pass