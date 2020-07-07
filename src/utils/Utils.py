from datetime import date


class Utils(object):
    """Provides useful procedures for different contexts"""

    @staticmethod
    def format_uuid(unformatted_uuid):
        """Transforms an unformatted uuid into a formatted uuid"""

        formatted_uuid = unformatted_uuid[0:8]
        formatted_uuid = formatted_uuid + '-' + unformatted_uuid[8:12]
        formatted_uuid = formatted_uuid + '-' + unformatted_uuid[12:16]
        formatted_uuid = formatted_uuid + '-' + unformatted_uuid[16:20]
        formatted_uuid = formatted_uuid + '-' + unformatted_uuid[20:32]

        return formatted_uuid

    @staticmethod
    def date_format_from(value):
        """Checks if the date format is American or Brazilian"""
        
        original_value = value
        
        date_format = None

        # Checks if is an US date format
        value = value.split('-')

        value_len = len(value)

        if value_len == 3:

            date_format = 'US'

        else:

            # Checks if is an BR date format

            value = original_value

            value = value.split('/')

            value_len = len(value)

            if value_len == 3:

                date_format = 'BR'

        return date_format

    @staticmethod
    def us_string_date_format_to_date(value):

        value = value.split('-')        

        day = int(value[2])
        month = int(value[1])
        year = int(value[0])

        to_date = date(year, month, day)

        return to_date
        
    @staticmethod
    def br_string_date_format_to_date(value):

        value = value.split('-')        

        day = int(value[0])
        month = int(value[1])
        year = int(value[2])
        
        to_date = date(year, month, day)

        return to_date
        

    @staticmethod
    def float_to_string(value):
        """Transforms a float into a string considering 2 decimal places"""

        value = str(value)

        original = value.replace('.', '')

        value = value.split('.')

        if len(value) > 1:

            if len(value[1]) < 2:

                value = value[0] + value[1] + '0'

            else:

                return original

        else:

            return original

        return value

    @staticmethod
    def string_to_brazilian_currency(value, symbol=''):
        """Formats the value in Brazilian currency format"""
        BRL_value = ''

        value_len = 0

        if value == '':

            int_value = 0

        else:

            int_value = int(value)

        value_len = len(value)

        if value_len == 2:

            value = "0" + value

        elif value_len == 1:

            value = "00" + value

        elif int_value == 0:

            value = "000"

        control = 1

        for i in range(len(value)):

            if i == len(value) - 2:

                BRL_value = BRL_value + ","

            BRL_value = BRL_value + value[i]

            control = control + 1

        BRL_value = BRL_value.split(',')

        left_side = BRL_value[0]

        if len(left_side) > 3:

            new_left_side = ''

            control = 1

            for i in range(len(left_side)-1, -1, -1):

                if (control % 3 == 0) and (i != 0):

                    new_left_side = '.' + left_side[i] + new_left_side

                else:
                    new_left_side = left_side[i] + new_left_side

                control = control + 1

            left_side = new_left_side

        BRL_value = left_side + "," + BRL_value[1]

        BRL_value = symbol + " " + BRL_value

        return BRL_value
