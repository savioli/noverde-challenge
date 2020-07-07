from validation.core import Constraint
from utils import Utils


class ValueBetweenConstraint(Constraint):
    """"Checks if the value is within a certain range

    Attributes:
        min_value    The set
        max_value    The type of elements contained in the set
    """

    def __init__(self):
        """Creates a ValueBetweenConstraint initializing the attributes"""

        super().__init__()

        self.min_value = None

        self.max_value = None

    def validate(self, value):
        """Validates the constraint"""

        if type(value) == str:

            value = float(value)

        if (value < self.min_value):

            error_message = 'O valor informado deve ser maior ou igual a {}.'

            value_as_currency = Utils.float_to_string(self.min_value)
            value_as_currency = Utils.string_to_brazilian_currency(value_as_currency, 'R$')

            error_message = error_message.format(value_as_currency)

            self.errors.append(error_message)

        if (value > self.max_value):

            error_message = 'O valor informado de ser menor ou igual a {}.'

            value_as_currency = Utils.float_to_string(self.max_value)
            value_as_currency = Utils.string_to_brazilian_currency(value_as_currency, 'R$')

            error_message = error_message.format(value_as_currency)

            self.errors.append(error_message)

        return self.errors
