from abc import ABC, abstractmethod

class Constraint(ABC):
    """A base class to a Constraint

    Attributes:
        errors    A list of erros that breaks the constraint
    """

    def __init__(self):
        """Creates a Constraint initializing the attributes"""
        
        self.errors = []

    @abstractmethod
    def validate(self, value):
        """The logic of the constraint to be validated"""
        pass
