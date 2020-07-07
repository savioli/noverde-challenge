import unittest
from noverde import NoverdeClient


class TestNoverdeClient(unittest.TestCase):
    """Test the capabilities of the Noverde Client"""

    def test_score_with_simulated_endpoint(self):
        """
        Test the score service using a valid CPF 
        in the simulated endpoint
        """

        noverde = NoverdeClient()

        cpf = '54830143088'

        score = noverde.get_score(cpf)

        # Checks if the value is greater than or equal to 0
        self.assertGreaterEqual(score, 0)

        # Checks if the value is less than or equal to 1000
        self.assertLessEqual(score, 1000)

    def test_commitment_simulated_endpoint(self):
        """
        Test the commitment service using a valid CPF 
        in the simulated endpoint
        """
        noverde = NoverdeClient()

        cpf = '54830143088'

        commitment = noverde.get_commitment(cpf)

        # Checks if the value is less than or equal to 0
        self.assertGreaterEqual(commitment, 0.0)

        # Checks if the value is less than or equal to 1.0
        self.assertLessEqual(commitment, 1.0)

    # def test_score_real_endpoint(self):
    #     """
    #     Test the score service using a valid CPF
    #     in the real endpoint
    #     """

    #     API_key = 'SnAB7jQEFs1Ai8XtZdssa14gORT3jWPI7TWdXN97'

    #     noverde = NoverdeClient(API_key)

    #     cpf = '54830143088'

    #     score = noverde.get_score(cpf)

    #     # Checks if the value is greater than or equal to 0
    #     self.assertGreaterEqual(score, 0)

    #     # Checks if the value is less than or equal to 1000
    #     self.assertLessEqual(score, 1000)

    # def test_commitment_real_endpoint(self):
    #     """
    #     Test the commitment service using a valid CPF
    #     in the real endpoint
    #     """

    #     API_key = 'SnAB7jQEFs1Ai8XtZdssa14gORT3jWPI7TWdXN97'

    #     noverde = NoverdeClient(API_key)

    #     cpf = '54830143088'

    #     commitment = noverde.get_commitment(cpf)

    #     # Checks if the value is greater than or equal to 0.0
    #     self.assertGreaterEqual(commitment, 0.0)

    #     # Checks if the value is less than or equal to 1.0
    #     self.assertLessEqual(commitment, 1.0)
