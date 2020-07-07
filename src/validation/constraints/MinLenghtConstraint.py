from validation.core import Constraint


class MinLenghtConstraint(Constraint):
    """Certifies if the value is greater than a certain value    
    
    Attributes:
        min_value    The set
    """

    def __init__(self):
        """Creates a MinLenghtConstraint initializing the attribute"""

        super().__init__()

        self.min_lenght = None

    def validate(self, value):
        """Validates the constraint"""

        value_len = len(value)

        if (value_len < self.min_lenght):

            error_message = 'O campo deve ter no mínimo {} caracteres.'.format(self.min_lenght)
            self.errors.append(error_message)

        return self.errors
