
import json
import requests
from random import randint
from requests import RequestException

from noverde.exceptions import NoverdeException, POSTRequestFailedException, BadResponseFormatException

class NoverdeClient(object):
    """A client to access the capabilities of the Noverde API"""

    # The default endpoint
    DEFAULT_ENDPOINT = 'https://challenge.noverde.name'

    # The default name to the attribute X-api-key
    X_API_KEY_ATTRIBUTE_NAME = 'x-api-key'

    # The default path to score entity
    SCORE_PATH = 'score'

    # The default path to commiment entity
    COMMITMENT_PATH = 'commitment'

    # The default name to the CPF
    CPF_ATTRIBUTE_NAME = 'cpf'

    # The default name to the attribute score
    SCORE_ATTRIBUTE_NAME = 'score'

    # The default name to the attribute commitment
    COMMITMENT_ATTRIBUTE_NAME = 'commitment'

    def __init__(self, API_key=None):
        """Constructs the object by optionally passing an API key"""

        self.API_key = API_key

        headers = dict()

        headers[self.X_API_KEY_ATTRIBUTE_NAME] = API_key

        self.headers = headers

    def post(self, entity_path, json):
        """Send a generic POST request"""

        url = self.DEFAULT_ENDPOINT + '/' + entity_path

        try:

            response = requests.post(url=url,
                                     json=json,
                                     headers=self.headers)

        except RequestException as e:

            raise POSTRequestFailedException('',e)

        if response.status_code == 200:
            # If the request returns code 200
            
            try:
                # Interprets the answer in json

                response = response.json()

            except ValueError as e:
                # If is not json, throw an exception

                raise BadResponseFormatException('',e)

            return response

        else:
            # If the request fails, throw an exception

            raise POSTRequestFailedException('',e)

    def get_score(self, cpf):
        """Gets the score given a CPF"""

        if self.API_key is not None:
            # If an API key is defined

            args = dict()

            args[self.CPF_ATTRIBUTE_NAME] = cpf

            try:
    
                # Send a request
                response = self.post(self.SCORE_PATH, args)

            except NoverdeException as e:

                raise NoverdeException('',e)

            score = response[self.SCORE_ATTRIBUTE_NAME]

            return score

        else:
            # If there is no defined API key,
            # the Noverde Web Service enters in simulation mode.
            # Warning: This is only for development purposes.

            score = randint(0, 1000)

            return score

    def get_commitment(self, cpf):
        """Gets the commitment given a CPF"""

        if self.API_key is not None:
            # If an API key is defined

            args = dict()

            args[self.CPF_ATTRIBUTE_NAME] = cpf

            # Send a request
            response = self.post(self.COMMITMENT_PATH, args)

            commitment = response[self.COMMITMENT_ATTRIBUTE_NAME]

            return commitment

        else:
            # If there is no defined API key,
            # the Noverde Web Service enters in simulation mode.
            # Warning: This is only for development purposes.

            # Generate a number between 0 and 100
            commitment = randint(0, 100)

            # And is divided by 100 to return a number between 0.0 and 1.0
            commitment = commitment/100

            return commitment
