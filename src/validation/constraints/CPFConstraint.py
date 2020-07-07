from validation.core import Constraint


class CPFConstraint(Constraint):
    """Checks if it is a valid CPF
    
    Constants:
    
        CPF_LENGTH    The length of a CPF
    """

    CPF_LENGTH = 11

    def validate(self, value):
        """Validates the constraint"""

        value_len = len(value)

        control = 0

        all_equal = True

        for control in range(CPFConstraint.CPF_LENGTH-1):

            if value[control] != value[control+1]:

                all_equal = False

                break

        if (value_len != CPFConstraint.CPF_LENGTH) or (all_equal == True):

            error_message = 'O CPF informado é inválido.'
            self.errors.append(error_message)

        else:

            for t in range(9, CPFConstraint.CPF_LENGTH):

                d = 0
                c = 0

                while c < t:

                    d = d + (int(value[c]) * ((t+1)-c))

                    c = c + 1

                d = ((10*d) % 11) % 10

                if int(value[c]) != d:

                    error_message = 'O CPF informado é inválido.'
                    self.errors.append(error_message)

                    break

        return self.errors
