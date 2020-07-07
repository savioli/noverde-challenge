from datetime import date
from business.policies import CreditPolicy
from business.policies.exceptions import MandatoryCreditPolicyArgumentNotFoundException, InvalidCreditPolicyArgumentTypeException


class AgeCreditPolicy(CreditPolicy):
    """An age-based Credit Policy

    Attributes:
        age    An age for the policy

    Constants:

        CREDIT_POLICY_SHORT_NAME    The credit police short name
        CREDIT_POLICY_FULL_NAME     The credit police fullname
        DEFAULT_AGE                 A default age for the policy
    """

    CREDIT_POLICY_SHORT_NAME = 'Age'
    CREDIT_POLICY_FULL_NAME = 'AgeCreditPolicy'
    DEFAULT_AGE = 18

    def __init__(self):
        """Creates the policy with the default age"""

        self.age = self.DEFAULT_AGE

    def evaluate(self, args):
        """Evaluates the policy"""

        try:
            
            # Checks if the args['birthdate'] was sent
            birthdate = args['birthdate']

        except KeyError as e:

            raise MandatoryCreditPolicyArgumentNotFoundException('', e)

        
        if not isinstance(birthdate, date):
            # Checks if the score is of type date
            raise InvalidCreditPolicyArgumentTypeException()

        today = date.today()

        age = today.year - birthdate.year

        # Return based in the bussiness rule
        if age > self.age:

            return True

        elif age < self.age:

            return False

        else:

            if today.month > birthdate.month:

                return True

            elif today.month < birthdate.month:

                return False

            else:

                if today.day >= birthdate.day:

                    return True

                else:

                    return False
