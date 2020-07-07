import re
from validation.core import Constraint


class UUIDConstraint(Constraint):
    """Checks if it is a valid UUID"""

    def validate(self, value):
        """Validates the constraint"""

        uuid_formatted = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
        uuid_unformatted = '[0-9a-f]{32}'

        uuid_pattern = '(' + uuid_formatted + '|' + uuid_unformatted + ')'

        value = str(value)

        result = re.match(uuid_pattern, value, re.MULTILINE)

        if result is None:

            error_message = 'O valor informado {} não é um UUID válido.'.format(
                value)
            self.errors.append(error_message)

        return self.errors
