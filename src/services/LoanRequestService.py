import uuid as uuid_generator

from models import LoanRequest
from business.policies import AgeCreditPolicy, ScoreCreditPolicy, CommitmentCreditPolicy
from business.policies.exceptions import CreditPolicyException, CommitmentCreditPolicyException
from noverde.exceptions import NoverdeException
from services.exceptions import LoanRequestServiceException
from database.exceptions import LoanRequestDBException
from tasks import EvaluatePoliciesTask, QueueException

class LoanRequestService(object):
    """Provide operations related with LoanRequest entity

    Attributes:
        database    An DataBase implementation
        queue       The Queue implementation
    """

    def __init__(self, database=None, queue=None):
        """
        Constructs the object by optionally passing 
        a DataBase implementation and/or a Queue implementation 
        """

        self.database = None

        self.queue = None
        
        self.noverde = None

    def save_loan_request(self, loan_request):
        """Persists a LoanRequest"""

        # Generate a new UUID for the Loan Request

        uuid = uuid_generator.uuid4()

        uuid = str(uuid)

        uuid = uuid.replace('-','')

        loan_request.uuid = uuid

        # Set the PROCESSING_STATE
        loan_request.result = LoanRequest.PROCESSING_STATE

        try:

            loan_request = self.database.save_loan_request(loan_request)

        except LoanRequestDBException as e:

            raise LoanRequestServiceException('', e)

        return loan_request

    def get_loan_request_by_uuid(self, uuid):
        """Gets a LoanRequest given an UUID"""

        try:
            
            loan_request = self.database.get_loan_request_by_uuid(uuid)

        except LoanRequestDBException as e:

            raise LoanRequestServiceException('', e)

        return loan_request

    def update_loan_request(self, loan_request):
        """Updates a LoanRequest"""

        try:

            loan_request = self.database.update_loan_request(loan_request)

        except LoanRequestDBException as e:

            raise LoanRequestServiceException('', e)

        return loan_request

    def enqueue_loan_request(self, loan_request):
        """Queues a LoanRequest for background processing"""

        uuid = loan_request.uuid

        try:

            evaluate_policies_task = EvaluatePoliciesTask()
            
            self.queue.tasks.register(evaluate_policies_task)

            evaluate_policies_task.delay(uuid)

        except QueueException as e:

            raise LoanRequestServiceException('', e)

    def evaluate_policies(self, loan_request):
        """Processes the loan policies based on LoanRequest information"""

        # Verify the Age Credit Policy using: birthdate

        # Defines the params requested by the policy
        args = dict()

        args['birthdate'] = loan_request.birthdate

        age_credit_policy = AgeCreditPolicy()
        
        # Configure the policy
        age_credit_policy.age = 18

        # Processes policy

        try:

            result = age_credit_policy.evaluate(args)

        except CreditPolicyException as e:

            raise LoanRequestServiceException('',e)

        if result == False:

            result = 'refused'

            loan_request.result = result

            refused_policy = AgeCreditPolicy.CREDIT_POLICY_SHORT_NAME.lower()

            loan_request.refused_policy = refused_policy

            loan_request.status = LoanRequest.COMPLETED_STATE

            # Returns completing policy processing
            return loan_request

        # Verify the Score Credit Policy using: cpf
        cpf = loan_request.cpf

        # Use the NOVERDE service to get the score relative to the CPF

        try:

            score = self.noverde.get_score(cpf)

        except NoverdeException as e:

            raise LoanRequestServiceException('', e)

        # Defines the params requested by the policy
        args = dict()

        args['score'] = score

        score_credit_policy = ScoreCreditPolicy()
        
        # Configure the policy
        score_credit_policy.passing_score = 600

        # Processes policy

        try:

            result = score_credit_policy.evaluate(args)

        except CreditPolicyException as e:

            raise LoanRequestServiceException('',e)

        if result == False:

            result = 'refused'

            loan_request.result = result

            refused_policy = ScoreCreditPolicy.CREDIT_POLICY_SHORT_NAME.lower()

            loan_request.refused_policy = refused_policy

            loan_request.status = LoanRequest.COMPLETED_STATE

            # Returns completing policy processing
            return loan_request

        # Verify the Commitment Credit Policy
        # using: score, commitment, income, terms, amount

        # Use the NOVERDE service to get the commitment relative to the CPF
        try:

            commitment = self.noverde.get_commitment(cpf)

        except NoverdeException as e:

            raise LoanRequestServiceException('', e)

        # Defines the params requested by the policy
        args = dict()

        args['commitment'] = commitment
        args['income'] = loan_request.income
        args['terms'] = loan_request.terms
        args['amount'] = loan_request.amount
        args['score'] = score

        commitment_credit_policy = CommitmentCreditPolicy()

        matrix = [ {
                    'score_range': (900, 1000), 
                    'interests': { 6  : 3.9, 
                                   9  : 4.2,
                                   12 : 4.5} 
                   },
                   {
                    'score_range': (800,  899),
                    'interests': { 6  : 4.7, 
                                   9  : 5.0, 
                                   12 : 5.3}
                   },
                   {
                    'score_range': (700,  799),
                    'interests': { 6  : 5.5, 
                                   9  : 5.8, 
                                   12 : 6.1}
                   },
                   {
                    'score_range': (600,  699),
                    'interests': { 6  : 6.4, 
                                   9  : 6.6, 
                                   12 : 6.9}
                   }
                 ]

        commitment_credit_policy.interest_matrix = matrix

        # Processes policy

        try:

            result = commitment_credit_policy.evaluate(args)

        except CommitmentCreditPolicyException as e:

            raise LoanRequestServiceException('',e)

        if result == False:

            result = 'refused'

            refused_policy = CommitmentCreditPolicy.CREDIT_POLICY_SHORT_NAME.lower()

            loan_request.result = result

            loan_request.refused_policy = refused_policy

            loan_request.status = LoanRequest.COMPLETED_STATE

        else:

            result = 'approved'

            loan_request.result = result

            loan_request.approved_amount = commitment_credit_policy.approved_amount

            loan_request.approved_terms = commitment_credit_policy.approved_terms

            loan_request.status = LoanRequest.COMPLETED_STATE

        # Returns completing policy processing
        return loan_request