import unittest
from validation.constraints import BirthdateConstraint


class TestBirthdateConstraint(unittest.TestCase):
    """Tests cases for BirthdateConstraint"""

    def test_valid_us_format_date(self):
        """Tests valid American date format"""

        constraint = BirthdateConstraint()

        date = '2010-06-18'

        errors = constraint.validate(date)

        errors_len = len(errors)

        self.assertEqual(errors_len, 0)

    def test_valid_br_format_date(self):
        """Tests valid Brazilian date format"""

        constraint = BirthdateConstraint()

        date = '09/06/2010'

        errors = constraint.validate(date)

        errors_len = len(errors)

        self.assertEqual(errors_len, 0)
