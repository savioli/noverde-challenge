from loan.amortization import Amortization
from loan.amortization.exceptions import AmortizationNotConfiguredException

class PRICEAmortization (Amortization):
    """Implements the PRICE amortization method"""

    def __init__(self):
        """Creates the method initializing the attributes"""

        self.configured = False

        self.time_in_months = 0

        self.present_value = 0

        self.interest_rate = 0

        self.precision = 2

    def configure(self, interest_rate, present_value, time_in_months, precision=2):
        """Configure the parameters for the amortization method"""

        self.time_in_months = time_in_months
        self.present_value = present_value
        self.interest_rate = interest_rate
        self.precision = precision

        self.interest_rate = self.interest_rate / 100

        self.configured = True

    def installment_amount(self):
        """Calculates the value of the installment based in the given parameters to the method"""
        if self.configured == True:

            self.current_installment_amount = self.present_value * \
                ((((1 + self.interest_rate) ** self.time_in_months) * self.interest_rate) /
                 (((1 + self.interest_rate) ** self.time_in_months) - 1))

            return round(self.current_installment_amount, 2)

        else:

            # Amortization System Not Configured
            raise AmortizationNotConfiguredException()
