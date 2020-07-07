import unittest
from business.policies import ScoreCreditPolicy


class TestScoreCreditPolicy(unittest.TestCase):
    """Tests cases for ScoreCreditPolicy"""

    def test_min_score_for_an_aprovation(self):
        """Tests the lowest score value for an approval"""

        credit_policy = ScoreCreditPolicy()

        args = dict()

        # In the future, this value can be retrieved from database
        args['score'] = 600

        result = credit_policy.evaluate(args)

        self.assertTrue(result)

    def test_max_score_for_reprovation(self):
        """Tests the highest score value for a failure"""

        credit_policy = ScoreCreditPolicy()

        args = dict()

        # In the future, this value can be retrieved from database
        args['score'] = 599

        result = credit_policy.evaluate(args)

        self.assertFalse(result)

    def test_mandatory_argument_not_present(self):
        """Tests the case where the mandatory arguments are not passed"""

        credit_policy = ScoreCreditPolicy()

        args = dict()

        with self.assertRaises(Exception):
            result = credit_policy.evaluate(args)

    def test_invalid_argument_type(self):
        """Tests the case where the argument type is invalid"""

        credit_policy = ScoreCreditPolicy()

        args = dict()

        args['score'] = '600'

        with self.assertRaises(Exception):
            result = credit_policy.evaluate(args)
