import unittest
from business.policies import CommitmentCreditPolicy


class TestCommitmentCreditPolicy(unittest.TestCase):
    """Tests cases for CommitmentCreditPolicy"""
    
    def test_approved_evaluation(self):
        """Tests the case of a loan application that will be approved"""

        args = dict()

        args['commitment'] = 0.8
        args['income'] = 1500.00
        args['terms'] = 6
        args['amount'] = 2500.00
        args['score'] = 750

        commitment_credit_policy = CommitmentCreditPolicy()

        commitment_credit_policy.interest_matrix = [
            {'score_range': (900, 1000),
             'interests': {6: 3.9, 9: 4.2, 12: 4.5}},
            {'score_range': (800,  899),
             'interests': {6: 4.7, 9: 5.0, 12: 5.3}},
            {'score_range': (700,  799),
             'interests': {6: 5.5, 9: 5.8, 12: 6.1}},
            {'score_range': (600,  699),
             'interests':  {6: 6.4, 9: 6.6, 12: 6.9}}
        ]

        result = commitment_credit_policy.evaluate(args)

        self.assertTrue(result)

    def test_reproved_evaluation(self):
        """Tests the case of a loan application that will fail"""

        args = dict()

        args['commitment'] = 1.0
        args['income'] = 1500.00
        args['terms'] = 6
        args['amount'] = 4000.00
        args['score'] = 750

        commitment_credit_policy = CommitmentCreditPolicy()

        commitment_credit_policy.interest_matrix = [
            {'score_range': (900, 1000),
             'interests': {6: 3.9, 9: 4.2, 12: 4.5}},
            {'score_range': (800,  899),
             'interests': {6: 4.7, 9: 5.0, 12: 5.3}},
            {'score_range': (700,  799),
             'interests': {6: 5.5, 9: 5.8, 12: 6.1}},
            {'score_range': (600,  699),
             'interests':  {6: 6.4, 9: 6.6, 12: 6.9}}
        ]

        result = commitment_credit_policy.evaluate(args)

        self.assertFalse(result)

    def test_no_interest_matrix_evaluation(self):
        """Tests the case where the interest matrix has not been passed"""

        args = dict()

        args['commitment'] = 1.0
        args['income'] = 1500.00
        args['terms'] = 6
        args['amount'] = 4000.00
        args['score'] = 750

        commitment_credit_policy = CommitmentCreditPolicy()

        with self.assertRaises(Exception):
            result = commitment_credit_policy.evaluate(args)

    def test_interest_matrix_bad_format(self):
        """Tests the case where the interest matrix has a different format"""
        
        args = dict()

        args['commitment'] = 1.0
        args['income'] = 1500.00
        args['terms'] = 6
        args['amount'] = 4000.00
        args['score'] = 750

        commitment_credit_policy = CommitmentCreditPolicy()

        commitment_credit_policy.interest_matrix = [
            {'score_range_bad_format': (900, 1000),
             'interests': {6: 3.9, 9: 4.2, 12: 4.5}},
            {'score_range_bad_format': (800,  899),
             'interests': {6: 4.7, 9: 5.0, 12: 5.3}},
            {'score_range_bad_format': (700,  799),
             'interests': {6: 5.5, 9: 5.8, 12: 6.1}},
            {'score_range_bad_format': (600,  699),
             'interests':  {6: 6.4, 9: 6.6, 12: 6.9}}
        ]
        with self.assertRaises(Exception):
            result = commitment_credit_policy.evaluate(args)
