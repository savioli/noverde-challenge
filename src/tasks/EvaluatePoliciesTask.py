import os
from celery import Task
from celery.exceptions import Retry
from celery.states import FAILURE, RETRY

from services import LoanRequestService
from services.exceptions import LoanRequestServiceException
from database import LoanRequestMongoDBImpl
from pymongo import MongoClient
from noverde import NoverdeClient

class EvaluatePoliciesTask(Task):
    """Task to process the loan policies based on LoanRequest information"""

    def __init__(self):
        """Creates a task"""
        
        # Defines the task name
        self.name = 'EvaluatePoliciesTask'

    def run(self, uuid):
        """Executes the task"""
        

        loan_request_service = LoanRequestService()

        # Stores the Loan Request in a DataBase

        mongodb_hostname = os.environ['MONGODB_HOSTNAME']

        mongodb_uri = 'mongodb://' + mongodb_hostname + ':27017'
        
        connection = MongoClient(mongodb_uri)

        database = LoanRequestMongoDBImpl(connection)

        # TODO EXCEPTION
        loan_request_service.database = database

        try:

            # Get the LoanRequest
            loan_request = loan_request_service.get_loan_request_by_uuid(uuid)

            if os.environ['X_API_KEY'] == '':

                API_KEY = None

            else:

                API_KEY = os.environ['X_API_KEY']

            # Set the noverde client
            
            loan_request_service.noverde = NoverdeClient(API_KEY)
            
            # Evaluate Policies of the LoanRequest
            loan_request = loan_request_service.evaluate_policies(loan_request)

            # Update the LoanRequest with the result of the evaluated policies
            loan_request = loan_request_service.update_loan_request(loan_request)

        except LoanRequestServiceException as e:

            message = str(e)

            meta = dict()

            meta['Exception'] = message

            self.update_state(state=RETRY, meta=meta)
            
            raise Retry()

        result = loan_request.result

        return result
