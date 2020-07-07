import os
import json

from flask import current_app as app
from flask import request
from flask.views import MethodView
from pymongo import MongoClient
from models import LoanRequest
from services import LoanRequestService
from services.exceptions import LoanRequestServiceException
from database import LoanRequestMongoDBImpl
from celery import Celery
from validation.contexts import LoanRequestGETContextValidator
from validation.contexts import LoanRequestPOSTContextValidator
from datetime import date
from utils import Utils
from noverde import NoverdeClient


class LoanRequestController(MethodView):
    """Controller to respond to the API methods for a LoanRequest"""

    def post(self):
        """Respond to a LoanRequest returning a Request Schema"""

        # Verify if all mandatory fields have been sent

        request_args = []

        if request.method == 'POST':

            request_params = request.form

        else:

            request_params = request.args

        for key in request_params.keys():

            request_args.append(key)

        mandatory_fields = ['name',
                            'cpf',
                            'amount',
                            'birthdate',
                            'terms',
                            'income']

        missing_fields = set(mandatory_fields) - set(request_args)

        missing_fields_len = len(missing_fields)

        errors = dict()

        if missing_fields_len == 0:
            # If there is no missing field we proceed with the validation
            # of these fields

            params = dict()

            # Do a simple sanitization

            for key in mandatory_fields:

                params[key] = request_params.get(key)
                params[key] = params[key].strip()

            # Removes the dots and the hyphen from the CPF if it's present
            params['cpf'] = params['cpf'].replace('-', '')
            params['cpf'] = params['cpf'].replace('.', '')

            # Create a new validator for the params of the request
            validator = LoanRequestPOSTContextValidator()

            # Validate this params
            validator.validate(params)

            is_valid = validator.is_valid()

            if is_valid:
                
                # If all fields are valid proceed

                # Create a new LoanRequest to be validated
                loan_request = LoanRequest()

                name = params['name']
                loan_request.name = name

                birthdate = params['birthdate']

                date_format = Utils.date_format_from(birthdate)

                if date_format == 'US':
                    
                    loan_request.birthdate = Utils.us_string_date_format_to_date( birthdate )
                    
                elif date_format == 'BR':

                    loan_request.birthdate = Utils.br_string_date_format_to_date( birthdate )

                cpf = params['cpf']
                loan_request.cpf = cpf

                amount = float(params['amount'])
                loan_request.amount = amount

                terms = int(params['terms'])
                loan_request.terms = terms

                income = float(params['income'])
                loan_request.income = income

                loan_request_service = LoanRequestService()

                # Stores the Loan Request in a DataBase

                config_storage = app.config['STORAGE']

                if config_storage == 'mongodb':

                    mongodb_hostname = app.config['MONGODB_HOSTNAME']

                    mongodb_uri = 'mongodb://' + mongodb_hostname + ':27017'

                    connection = MongoClient(mongodb_uri)

                    database = LoanRequestMongoDBImpl(connection)

                    loan_request_service.database = database

                elif config_storage == 'dynamodb':

                    # Create an instance of dynamoDB implementation
                    pass

                try:

                    loan_request = loan_request_service.save_loan_request(loan_request)

                except LoanRequestServiceException as e:

                    json_response = ['Internal Error']

                    json_response = json.dumps(['Internal Error'])

                    return (json_response, 500, {'Content-Type': 'application/json'})

                MODE = app.config['MODE']

                if MODE == 'sync':

                    try:

                        # Set the noverde client
                        API_KEY = app.config['X_API_KEY']

                        loan_request_service.noverde = NoverdeClient(API_KEY)

                        # Evaluate Policies of the LoanRequest
                        loan_request = loan_request_service.evaluate_policies(loan_request)

                    except LoanRequestServiceException as e:

                        json_response = ['Internal Error']

                        json_response = json.dumps(['Internal Error'])

                        return (json_response, 500, {'Content-Type': 'application/json'})

                    try:

                        # Update the LoanRequest with the result of the evaluated policies
                        loan_request = loan_request_service.update_loan_request(loan_request)

                    except LoanRequestServiceException as e:

                        json_response = ['Internal Error']

                        json_response = json.dumps(['Internal Error'])

                        return (json_response, 500, {'Content-Type': 'application/json'})

                elif MODE == 'async':

                    # Sends to process in background

                    redis_hostname = app.config['REDIS_HOSTNAME']

                    celery_backend_uri = 'redis://' + redis_hostname

                    rabbitmq_username = app.config['RABBITMQ_DEFAULT_USER']
                    rabbitmq_password = app.config['RABBITMQ_DEFAULT_PASS']
                    rabbitmq_hostname = app.config['RABBITMQ_HOSTNAME']

                    celery_broker_uri = 'amqp://' + rabbitmq_username + ':' + rabbitmq_password
                    celery_broker_uri = celery_broker_uri + '@' + rabbitmq_hostname
                    celery_broker_uri = celery_broker_uri + ':' + '5672'

                    queue = Celery('tasks',
                                   backend=celery_backend_uri,
                                   broker=celery_broker_uri)

                    loan_request_service.queue = queue

                    loan_request_service.enqueue_loan_request(loan_request)

                # If everything goes fine, then sends the response with the ID

                # Create a simple response just containing the new id generated

                json_response = dict()

                formatted_uuid = Utils.format_uuid(loan_request.uuid)

                json_response['id'] = formatted_uuid

                return (json_response, 200, {'Content-Type': 'application/json'})

            else:

                # Gets the list with the errors of each attribute
                errors_per_field = validator.get_errors()

                error_list = []

                for key, errors in errors_per_field.items():

                    for error in errors:

                        key = key.upper()

                        error_message = "{} - {}"

                        error_message = error_message.format(key, error)

                        error_list.append(error_message)

                errors = dict()

                errors['errors'] = error_list

                json_response = json.dumps(errors, indent=4)

                return (json_response, 400, {'Content-Type': 'application/json'})
        else:

            error_list = []

            for missing_field in missing_fields:

                message = '{} - O campo \'{}\' é necessário.'

                missing_field_upper = missing_field.upper()

                message = message.format(missing_field_upper, missing_field)

                error_list.append(message)

            errors = dict()

            errors['errors'] = error_list

            json_response = json.dumps(errors, indent=4)

            return (json_response, 400, {'Content-Type': 'application/json'})

    def get(self, uuid=None):
        """Respond to a consult returning a Response Schema"""

        if uuid == None:
            
            # If uuid parameter is not passed

            json_response = ''

            return (json_response, 400, {'Content-Type': 'application/json'})

        params = dict()
        params['uuid'] = uuid

        validator = LoanRequestGETContextValidator()

        validator.validate(params)

        is_valid = validator.is_valid()

        if is_valid:

            # Creates a database and the service
            mongodb_hostname = app.config['MONGODB_HOSTNAME']

            mongodb_uri = 'mongodb://' + mongodb_hostname + ':27017'

            connection = MongoClient(mongodb_uri)

            database = LoanRequestMongoDBImpl(connection)

            loan_request_service = LoanRequestService()

            loan_request_service.database = database

            try:

                # Get the LoanRequest

                uuid = uuid.replace('-', '')

                loan_request = loan_request_service.get_loan_request_by_uuid(
                    uuid)

            except LoanRequestServiceException as e:

                # If the LoanRequest was not found

                json_response = ''

                return (json_response, 404, {'Content-Type': 'application/json'})

            json_response = dict()
            formatted_uuid = Utils.format_uuid(loan_request.uuid)

            json_response['id'] = formatted_uuid
            json_response['status'] = loan_request.status
            json_response['result'] = loan_request.result
            json_response['refused_policy'] = loan_request.refused_policy
            json_response['approved_amount'] = loan_request.approved_amount
            json_response['approved_terms'] = loan_request.approved_terms

            # Format output
            json_response = json.dumps(json_response, indent=4)

            return (json_response, 200, {'Content-Type': 'application/json'})

        else:

            # If the LoanRequest was not found
            error_message = dict()
            error_message['errors'] = ['UUID inválido']

            json_response = json.dumps(error_message, indent=4)

            return (json_response, 400, {'Content-Type': 'application/json'})
