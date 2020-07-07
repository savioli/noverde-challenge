from business.policies import CreditPolicy
from business.policies.exceptions import NoInterestInTheRangeException
from business.policies.exceptions import InvalidCreditPolicyArgumentTypeException
from business.policies.exceptions import MandatoryCreditPolicyArgumentNotFoundException
from business.policies.exceptions import InvalidCommitmentCreditPolicyInterestMatrixException
from loan.amortization import PRICEAmortization


class CommitmentCreditPolicy(CreditPolicy):
    """A credit policy based in the income commitment

    Attributes:
        interests_matrix    An age for the policy
        approved_amount     An age for the policy
        approved_terms      An age for the policy

    Constants:

        CREDIT_POLICY_SHORT_NAME    The credit police short name
        CREDIT_POLICY_FULL_NAME     The credit police fullname
        DEFAULT_AGE                 A default age for the policy
    """

    CREDIT_POLICY_SHORT_NAME = 'Commitment'
    CREDIT_POLICY_FULL_NAME = 'CommitmentCreditPolicy'

    def __init__(self):
        """Creates the policy initializing the attributes"""

        self.interest_matrix = None
        self.approved_amount = None
        self.approved_terms = None

    def evaluate(self, args):
        """Evaluates the policy"""

        # Checks if the args['commitment'] was sent
        try:

            commitment = args['commitment']

        except KeyError as e:

            raise MandatoryCreditPolicyArgumentNotFoundException('', e)

        # Checks if the commitment is of type int
        if not isinstance(commitment, float):

            raise InvalidCreditPolicyArgumentTypeException()

        # Checks if the args['income'] was sent
        try:

            income = args['income']

        except KeyError as e:

            raise MandatoryCreditPolicyArgumentNotFoundException('', e)

        # Checks if the income is of type int

        if not isinstance(income, float):

            raise InvalidCreditPolicyArgumentTypeException()

        # Checks if the args['terms'] was sent
        try:

            terms = args['terms']

        except KeyError as e:

            raise MandatoryCreditPolicyArgumentNotFoundException('', e)

        # Checks if the terms is of type int
        if not isinstance(terms, int):

            raise InvalidCreditPolicyArgumentTypeException()

        # Checks if the args['amount'] was sent
        try:

            amount = args['amount']

        except KeyError as e:

            raise MandatoryCreditPolicyArgumentNotFoundException('', e)

        # Checks if the amount is of type int
        if not isinstance(amount, float):

            raise InvalidCreditPolicyArgumentTypeException()

        # Checks if the args['score'] was sent
        try:

            score = args['score']

        except KeyError as e:

            raise MandatoryCreditPolicyArgumentNotFoundException('', e)

        # Checks if the score is of type int
        if not isinstance(score, int):

            raise InvalidCreditPolicyArgumentTypeException()

        # Calculates the non committed income
        non_committed_income = income - (income * commitment)

        # Checks the interest matrix

        # If the interests matrix was not set
        if self.interest_matrix == None:

            # InvalidInterestsMatrixException
            raise InvalidCommitmentCreditPolicyInterestMatrixException()

        # If the interests matrix is not a list
        if not isinstance(self.interest_matrix, list):

            # InvalidInterestsMatrixException
            raise InvalidCommitmentCreditPolicyInterestMatrixException()

        # Search the interest based on score

        interests = None

        for interests_per_score in self.interest_matrix:

            try:

                min_range = interests_per_score['score_range'][0]
                max_range = interests_per_score['score_range'][1]

            except Exception as e:

                # BadInterestsMatrixFormatException
                raise Exception()

            score_range = range(min_range, max_range + 1)

            if score in score_range:

                interests = interests_per_score['interests']

                break

        if interests is not None:

            amortization = PRICEAmortization()

            for term in interests.keys():

                if term >= terms:

                    # The current installments number, starting from the selected by the client
                    # terms = term

                    # Defines the interest rate based in the score
                    interest_rate = interests[term]

                    # Configures according with the loan request information
                    amortization.configure(interest_rate, amount, term)

                    # Calculates the loan installment amount
                    installment_amount = amortization.installment_amount()

                    # Checks if the installment will not be greather than the non committed income

                    if non_committed_income >= installment_amount:

                        self.approved_amount = amount
                        self.approved_terms = term

                        return True

            # If there is no range in which the uncommitted income
            # supports the value of the installment, disapproves the loan.

            return False

        else:

            # If there is no interest for the range raise an exception
            # because can be an error of the system
            # for example the range was registered
            # but have not been added interest for the respective range

            raise NoInterestInTheRangeException()
