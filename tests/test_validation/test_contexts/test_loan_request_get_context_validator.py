import unittest
from validation.contexts import LoanRequestGETContextValidator


class TestLoanRequestGETContextValidator(unittest.TestCase):
    """Test cases for LoanRequestGETContextValidator"""

    def test_valid_formatted_uuid(self):
        """Tests for a valid formatted uuid"""

        validator = LoanRequestGETContextValidator()

        params = dict()

        params['uuid'] = 'df40337e-5c81-4a53-98d8-c73949c8cf5d'

        validator.validate(params)

        is_valid = validator.is_valid()

        self.assertTrue(is_valid)

    def test_valid_unformatted_uuid(self):
        """Tests for a valid unformatted uuid"""

        validator = LoanRequestGETContextValidator()

        params = dict()

        params['uuid'] = 'df40337e5c814a5398d8c73949c8cf5d'

        validator.validate(params)

        is_valid = validator.is_valid()

        self.assertTrue(is_valid)

    def test_invalid_uuid(self):
        """Tests for an invalid uuid"""

        validator = LoanRequestGETContextValidator()

        params = dict()

        params['uuid'] = 'df40337e5c814a53-98d8c73949c8cf5d'

        validator.validate(params)

        is_valid = validator.is_valid()

        self.assertFalse(is_valid)
