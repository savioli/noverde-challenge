import re
from validation.core import Constraint


class DecimalValueConstraint(Constraint):
    """Checks if it is a valid decimal value
    
    Attributes:
        decimal_plates    The number of decimal plates
    """

    def __init__(self):
        """Creates a DecimalValueConstraint initializing the attribute"""

        super().__init__()

        self.decimal_plates = 2

    def validate(self, value):
        """Validates the constraint"""

        decimal_pattern = r"^[0-9]{1,}\.[0-9]{1,"
        decimal_pattern = decimal_pattern + str(self.decimal_plates)
        decimal_pattern = decimal_pattern + "}$"

        value = str(value)

        result = re.match(decimal_pattern, value, re.MULTILINE)

        if result is None:

            error_message = 'O valor informado {} não é um número decimal válido.'.format(
                value)
            self.errors.append(error_message)

        return self.errors
