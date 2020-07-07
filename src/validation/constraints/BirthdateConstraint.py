from datetime import date, MINYEAR, MAXYEAR
from validation.core import Constraint


class BirthdateConstraint(Constraint):
    """Checks if it is a valid birthdate"""

    def validate(self, value):
        """Validates the constraint"""

        original_value = value

        date_format = None

        # Checks if is an US date format
        value = value.split('-')

        value_len = len(value)

        if value_len == 3:

            date_format = 'US'

        else:

            value = original_value

            value = value.split('/')

            value_len = len(value)

            if value_len == 3:

                date_format = 'BR'

        if date_format == 'US':

            day = value[2]
            month = value[1]
            year = value[0]

        elif date_format == 'BR':

            day = value[0]
            month = value[1]
            year = value[2]

        if date_format is not None:
            
            if (day.isdecimal() == False) or (month.isdecimal() == False) or (year.isdecimal() == False):

                error_message = 'O valor informado não é uma data de nascimento válida.'
                self.errors.append(error_message)

            else:

                day = int(day)
                month = int(month)
                year = int(year)

                if (year < MINYEAR) or (year > MAXYEAR):

                    error_message = 'O valor informado não é uma data de nascimento válida.'
                    self.errors.append(error_message)

                else:

                    past_date = date(year, month, day)

                    today = date.today()

                    if past_date >= today:

                        error_message = 'O valor informado não é uma data de nascimento válida.'
                        self.errors.append(error_message)

        else:

            error_message = 'O valor informado não é uma data válida.'
            self.errors.append(error_message)

        return self.errors
