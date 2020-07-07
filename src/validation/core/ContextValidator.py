from abc import ABC, abstractmethod

class ContextValidator(ABC):
    """A base class to a ContextValidator
    
    Attributes:
        total_errors    The total number of errors
        errors          A dictionary containing indexes to lists of the errors of each field
    """

    def __init__(self):
        """Creates a ContextValidator initializing the attributes"""

        self.total_errors = 0

        self.errors = None

    @abstractmethod
    def validate(self, value):
        """The logic of the context to be validated"""
        pass

    def total_of_errors(self):
        """Counts the total of errors generated by the validation"""

        self.total_errors = 0

        for key in self.errors:

            self.total_errors = self.total_errors + len(self.errors[ key ])

        return self.total_errors

    def get_errors(self):
        """Return the errors"""

        return self.errors

    def is_valid(self):
        """Return if the validation process resulted or not in errors"""
        
        if self.errors is None :
            # If the method validate wasn't called yet return False.

            return False
        
        if self.total_errors == 0 :
            # If there is no errors.

            return True

        else:

            # Otherwise...
            return False