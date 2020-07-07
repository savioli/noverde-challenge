import unittest
from validation.constraints import CPFConstraint


class TestCPFConstraint(unittest.TestCase):
    """Tests cases for CPFConstraint"""

    def test_valid_cpf(self):
        """Tests a valid CPF"""

        constraint = CPFConstraint()

        cpf = '91804454036'

        errors = constraint.validate(cpf)

        errors_len = len(errors)

        self.assertEqual(errors_len, 0)

    def test_invalid_non_equal_cpf(self):
        """Tests a non equal digits invalid CPF"""

        constraint = CPFConstraint()

        cpf = '91804454035'

        errors = constraint.validate(cpf)

        errors_len = len(errors)

        self.assertGreater(errors_len, 0)

    def test_invalid_equal_cpf(self):
        """Tests all possibilities of invalid equal digits CPF"""

        # Generate all CPF's possibilities with equal digits
        cpfs = [str(i) * 11 for i in range(10)]

        # Test each case
        for cpf in cpfs:

            constraint = CPFConstraint()

            errors = constraint.validate(cpf)

            errors_len = len(errors)

            self.assertGreater(errors_len, 0)
