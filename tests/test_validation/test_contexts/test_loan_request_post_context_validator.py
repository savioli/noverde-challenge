import unittest
from validation.contexts import LoanRequestPOSTContextValidator


class TestLoanRequestPOSTContextValidator(unittest.TestCase):
    """Test cases for LoanRequestPOSTContextValidator"""

    def test_valid_user(self):
        """Tests for a valid user"""

        validator = LoanRequestPOSTContextValidator()

        params = dict()

        params['name'] = 'John Doe'
        params['birthdate'] = '1990-11-09'
        params['cpf'] = '18951664112'
        params['amount'] = '3000.00'
        params['terms'] = 12
        params['income'] = '6000.00'

        validator.validate(params)

        is_valid = validator.is_valid()

        self.assertTrue(is_valid)

    def test_invalid_user(self):
        """Tests an invalid user"""

        validator = LoanRequestPOSTContextValidator()

        params = dict()

        # Invalid name
        params['name'] = 'an'

        # Invalid birthdate
        params['birthdate'] = '3020-11-09'

        # Invalid CPF
        params['cpf'] = '18951664115'

        # Invalid amount
        params['amount'] = '3000.006'

        # Invalid terms
        params['terms'] = '10'

        # Invalid income
        params['income'] = '6000.006'

        validator.validate(params)

        # Verify if is valid
        is_valid = validator.is_valid()

        msg = 'The LoanRequestPOSTContextValidator is not valid.'
        self.assertFalse(is_valid, msg=msg)

        # Verify the quantity of errors
        total_of_errors = validator.total_of_errors()

        msg = 'The number of errors for LoanRequestPOSTContextValidator that returns valid must be 0.'

        self.assertEqual(total_of_errors, 6, msg=msg)
