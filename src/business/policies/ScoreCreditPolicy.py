from business.policies import CreditPolicy
from business.policies.exceptions import MandatoryCreditPolicyArgumentNotFoundException, InvalidCreditPolicyArgumentTypeException


class ScoreCreditPolicy(CreditPolicy):
    """An score-based Credit Policy

    Attributes:
        passing_score    The passing score

    Constants:

        CREDIT_POLICY_SHORT_NAME    The credit police short name
        CREDIT_POLICY_FULL_NAME     The credit police fullname
        DEFAULT_PASSING_SCORE       A default passing score for the policy
    """

    CREDIT_POLICY_SHORT_NAME = 'Score'
    CREDIT_POLICY_FULL_NAME = 'ScoreCreditPolicy'
    DEFAULT_PASSING_SCORE = 600

    def __init__(self):
        """Creates the policy with the default passing score"""

        self.passing_score = self.DEFAULT_PASSING_SCORE

    def evaluate(self, args):
        """Evaluates the policy"""

        try:
            
            # Checks if the args['score'] was sent
            score = args['score']

        except KeyError as e:

            raise MandatoryCreditPolicyArgumentNotFoundException('', e)

        
        if not isinstance(score, int):
            # Checks if the score is of type int

            raise InvalidCreditPolicyArgumentTypeException()

        # Return based in the bussiness rule
        if score < self.passing_score:

            return False

        else:

            return True
