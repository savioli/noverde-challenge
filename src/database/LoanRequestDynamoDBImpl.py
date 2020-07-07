from datetime import date 

from database import LoanRequestDB
from database.exceptions import LoanRequestDynamoDBException
from models import LoanRequest

class LoanRequestDynamoDBImpl(LoanRequestDB):

    def __init__(self):
        
        raise LoanRequestDynamoDBException('Not Implemented yet')
    
    def save_loan_request(self, loan_request):
        """Saves a LoanRequest in DynamoDB"""
        
        raise LoanRequestDynamoDBException('Not Implemented yet')

    def update_loan_request(self, loan_request):
        """Updates a LoanRequest in MongoDB"""

        raise LoanRequestDynamoDBException('Not Implemented yet')

    def get_loan_request_by_uuid(self, uuid):
        """Gets a LoanRequest by uuid in MongoDB"""

        raise LoanRequestDynamoDBException('Not Implemented yet')

    def to_loan_request(self, record):
        """Transforms a MongoDB record in a LoanRequest"""
        
        raise LoanRequestDynamoDBException('Not Implemented yet')
