from datetime import date

from database import LoanRequestDB
from models import LoanRequest
from database.exceptions import LoanRequestMongoDBException

class LoanRequestMongoDBImpl(LoanRequestDB):

    def __init__(self, connection):

        self.connection = connection

        self.database = self.connection['noverde']

        self.loan_requests = self.database['loan-request']

    def save_loan_request(self, loan_request):
        """Saves a LoanRequest in MongoDB"""

        to_save = loan_request.__dict__

        birthdate = to_save['birthdate']
        
        day = birthdate.day

        if birthdate.day <= 9 :

            day = str(day)

        else:
            day = '0' + str(day)

        month = str(birthdate.month)
        year = str(birthdate.year)

        to_save['birthdate'] = year + '-' + month + '-' + day

        self.loan_requests.insert_one(loan_request.__dict__)

        record = self.loan_requests.find_one({'uuid': loan_request.uuid})

        loan_request = self.to_loan_request(record)

        return loan_request

    def update_loan_request(self, loan_request):
        """Updates a LoanRequest in MongoDB"""

        to_save = loan_request.__dict__

        birthdate = to_save['birthdate']

        day = str(birthdate.day)
        month = str(birthdate.month)
        year = str(birthdate.year)

        to_save['birthdate'] = year + '-' + month + '-' + day

        result = self.loan_requests.update_one({'uuid': loan_request.uuid},
                                               {"$set": loan_request.__dict__})

        record = self.loan_requests.find_one({'uuid': loan_request.uuid})

        return self.to_loan_request(record)

    def get_loan_request_by_uuid(self, uuid):
        """Gets a LoanRequest by uuid in MongoDB"""

        record = self.loan_requests.find_one({'uuid': uuid})

        if record is not None:

            loan_request = self.to_loan_request(record)

        else:
            
            raise LoanRequestMongoDBException()

            return None

        return loan_request

    def to_loan_request(self, record):
        """Transforms a MongoDB record in a LoanRequest"""

        loan_request = LoanRequest()

        uuid = record['uuid']

        name = record['name']
        cpf = record['cpf']
        amount = record['amount']
        terms = record['terms']
        income = record['income']
        status = record['status']
        result = record['result']
        refused_policy = record['refused_policy']
        approved_terms = record['approved_terms']
        approved_amount = record['approved_amount']

        birthdate = record['birthdate']

        birthdate = birthdate.split('-')

        day = int(birthdate[2])
        month = int(birthdate[1])
        year = int(birthdate[0])

        loan_request.birthdate = date(year, month, day)

        if uuid is not None:
            loan_request.uuid = record['uuid']

        if name is not None:
            loan_request.name = record['name']

        if cpf is not None:
            loan_request.cpf = record['cpf']

        if amount is not None:
            loan_request.amount = float(record['amount'])

        if terms is not None:
            loan_request.terms = int(record['terms'])

        if income is not None:
            loan_request.income = float(record['income'])

        if status is not None:
            loan_request.status = record['status']

        if result is not None:
            loan_request.result = record['result']

        if refused_policy is not None:
            loan_request.refused_policy = record['refused_policy']

        if approved_amount is not None:
            loan_request.approved_amount = float(record['approved_amount'])

        if approved_terms is not None:
            loan_request.approved_terms = int(record['approved_terms'])

        return loan_request
