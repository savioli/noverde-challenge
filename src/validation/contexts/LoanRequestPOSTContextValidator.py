from validation.core import ContextValidator
from validation.constraints import *


class LoanRequestPOSTContextValidator(ContextValidator):
    """The validator for the context of the POST of a LoanRequest"""

    def validate(self, params):
        """The validator for the context of the POST of a LoanRequest"""

        errors = dict()

        # Validates the name attribute
        min_lenght_constraint = MinLenghtConstraint()

        # Define the min lenght
        min_lenght_constraint.min_lenght = 3

        # Do the validation for the attribute
        name_errors = min_lenght_constraint.validate(params['name'])

        name_errors_len = len(name_errors)

        if name_errors_len > 0:

            errors['name'] = name_errors

        # Validates the name attribute
        cpf_constraint = CPFConstraint()

        # Do the validation for the attribute
        cpf_errors = cpf_constraint.validate(params['cpf'])

        cpf_errors_len = len(cpf_errors)

        if cpf_errors_len > 0:

            errors['cpf'] = cpf_errors

        # Validates the birthdate attribute
        birthdate_constraint = BirthdateConstraint()

        # Do the validation for the attribute
        birthdate_errors = birthdate_constraint.validate(params['birthdate'])

        birthdate_errors_len = len(birthdate_errors)

        if birthdate_errors_len > 0:

            errors['birthdate'] = birthdate_errors

        # Validates the terms attribute
        value_in_set_constraint = ValueIsInSetConstraint()

        # Define the set
        value_in_set_constraint.set = [6, 9, 12]

        # Define the type o the elements of the set
        value_in_set_constraint.type = int

        # Do the validation for the attribute
        terms_errors = value_in_set_constraint.validate(params['terms'])

        terms_errors_len = len(terms_errors)

        if terms_errors_len > 0:

            errors['terms'] = terms_errors

        # Validates the amount attribute

        # Validates if the value is a valid decimal number
        decimal_value_constraint = DecimalValueConstraint()

        # Define the number of decimal plates to be considered
        decimal_value_constraint.decimal_plates = 2

        # Do the validation for the attribute
        amount_errors = decimal_value_constraint.validate(params['amount'])

        amount_errors_len = len(amount_errors)

        if amount_errors_len > 0:

            try:
                errors['amount'] = errors['amount'] + amount_errors
            except Exception as e:
                errors['amount'] = amount_errors
        else:

            # Validates if the value is in a determined interval
            value_between_constraint = ValueBetweenConstraint()

            # Define the interval
            value_between_constraint.min_value = 2000.00
            value_between_constraint.max_value = 4000.00

            # Do the validation for the attribute
            amount_errors = value_between_constraint.validate(params['amount'])

            amount_errors_len = len(amount_errors)

            if amount_errors_len > 0:

                errors['amount'] = amount_errors

        # Validates the income attribute
        decimal_value_constraint = DecimalValueConstraint()

        # Define the number of decimal plates to be considered
        decimal_value_constraint.decimal_plates = 2

        # Do the validation for the attribute
        income_errors = decimal_value_constraint.validate(params['income'])

        income_errors_len = len(income_errors)

        if income_errors_len > 0:

            errors['income'] = income_errors

        self.errors = errors

        self.total_of_errors()
