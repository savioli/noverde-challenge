
from business.policies import AgeCreditPolicy
import unittest
from datetime import date


class TestAgeCreditPolicy(unittest.TestCase):
    """Tests cases for AgeCreditPolicy"""

    def test_valid_age(self):
        """Tests the policy for a valid age"""

        credit_policy = AgeCreditPolicy()

        args = dict()

        today = date.today()

        age = 18

        year = today.year-age

        month = today.month

        # 1 day until reaching the minimum age of the policy
        day = today.day-1

        past_date = date(year, month, day)

        args['birthdate'] = past_date

        credit_policy.age = age

        result = credit_policy.evaluate(args)

        self.assertTrue(result)

    def test_day_of_birthday(self):
        """Test Politics on Birthdate"""

        credit_policy = AgeCreditPolicy()

        args = dict()

        today = date.today()

        past_date = date(today.year-18, today.month, today.day)

        args['birthdate'] = past_date

        credit_policy.age = 18

        result = credit_policy.evaluate(args)

        self.assertTrue(result)

    def test_invalid_age(self):
        """Tests the policy for an invalid age"""

        credit_policy = AgeCreditPolicy()

        args = dict()

        today = date.today()

        age = 18

        year = today.year - age
        month = today.month
        day = today.day + 1

        past_date = date(year, month, day)

        args['birthdate'] = past_date

        credit_policy.age = age

        result = credit_policy.evaluate(args)

        self.assertFalse(result)

    def test_mandatory_argument_not_present(self):
        """Tests the case where the mandatory arguments are not passed"""

        credit_policy = AgeCreditPolicy()

        args = dict()

        with self.assertRaises(Exception):
            result = credit_policy.evaluate(args)

    def test_invalid_argument_type(self):
        """Tests the case where the argument type is invalid"""

        credit_policy = AgeCreditPolicy()

        args = dict()

        # The type must be a datetime.date
        
        args['birthdate'] = '1990-11-09'

        with self.assertRaises(Exception):
            result = credit_policy.evaluate(args)
