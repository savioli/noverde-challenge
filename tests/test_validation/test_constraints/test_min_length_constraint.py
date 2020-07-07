import unittest
from validation.constraints import MinLenghtConstraint


class TestLoanRequestContextValidator(unittest.TestCase):

    def test_valid_min_lenght_value(self):
        """Tests a valid CPF"""

        constraint = MinLenghtConstraint()

        value = 'John Doe'

        constraint.min_lenght = 3

        errors = constraint.validate(value)

        errors_len = len(errors)

        self.assertEqual(errors_len, 0)

    def test_invalid_min_lenght_exactly_lenght_value(self):
        """Tests a valid CPF"""

        constraint = MinLenghtConstraint()

        value = 'Ann'

        constraint.min_lenght = 3

        errors = constraint.validate(value)

        errors_len = len(errors)

        self.assertEqual(errors_len, 0)

    def test_invalid_min_lenght_value(self):
        """Tests a valid CPF"""

        constraint = MinLenghtConstraint()

        value = 'An'

        constraint.min_lenght = 3

        errors = constraint.validate(value)

        errors_len = len(errors)

        self.assertEqual(errors_len, 1)
