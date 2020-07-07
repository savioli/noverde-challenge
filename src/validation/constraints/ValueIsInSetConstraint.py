from validation.core import Constraint

class ValueIsInSetConstraint(Constraint):
    """Checks whether the value is contained in a given set
    
    Attributes:
        set    The set
        type   The type of elements contained in the set
    """
    
    def __init__(self):
        """Creates a ValueIsInSetConstraint initializing the attributes"""

        super().__init__()
        
        self.set = None

        self.type = None

    def validate(self, value):

        if not isinstance(value,self.type) :

            if self.type == int :

                try:
                    
                    value = int(value)

                except Exception as e:
                    
                    pass
            
        if value not in self.set :
          
            error_message = 'O valor {} não permitido.'
            error_message = error_message.format(value)
            self.errors.append( error_message )

        return self.errors
