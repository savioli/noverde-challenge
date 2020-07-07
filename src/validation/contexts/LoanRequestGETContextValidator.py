from validation.core import ContextValidator
from validation.constraints import UUIDConstraint


class LoanRequestGETContextValidator(ContextValidator):
    """The validator for the context of the GET of a LoanRequest"""

    def validate(self, params):
        """The validator for the context of the GET of a LoanRequest"""

        errors = dict()

        # Validates the UUID attribute
        uuid_constraint = UUIDConstraint()

        # Do the validation for the attribute
        uuid_errors = uuid_constraint.validate(params['uuid'])

        uuid_errors_len = len(uuid_errors)

        if uuid_errors_len > 0:

            errors['uuid'] = uuid_errors

        self.errors = errors

        self.total_of_errors()
