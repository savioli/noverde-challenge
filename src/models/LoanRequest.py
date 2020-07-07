class LoanRequest(object):
    """Class model representing a loan request

    Attributes:
        uuid              The universally unique identifier of the LoanRequest
        name              The name of the costumer
        birthdate         The birhtdate of the costumer
        amount            The amount requested by the costumer
        terms             The terms requested by the costumer
        income            The income of the costumer
        status            The status of the LoanRequest
        result            The result of the evaluation of the LoanRequest
        refused_policy    The policy that refused the Loan Request, if was refuse.
        approved_amount   The amount of the approved Loan Request.
        approved_terms    The terms of the approved Loan Request.

    Constants:
        PROCESSING_STATE  The processing state of the LoanRequest
        COMPLETED_STATE   The completed state of the LoanRequest
    """

    PROCESSING_STATE = 'processing'
    COMPLETED_STATE = 'completed'

    def __init__(self):

        # string
        self.uuid = None

        # string
        self.name = None

        # date
        self.birthdate = None

        # string
        self.cpf = None

        # float
        self.amount = None

        # integer
        self.terms = None

        # income
        self.income = None

        # string
        self.status = None

        # string
        self.result = None

        # string
        self.refused_policy = None

        # decimal
        self.approved_amount = None

        # decimal
        self.approved_terms = None
