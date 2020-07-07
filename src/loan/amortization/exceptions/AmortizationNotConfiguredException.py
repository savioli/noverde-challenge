from loan.amortization.exceptions import AmortizationException

class AmortizationNotConfiguredException(AmortizationException):
    """
    An exception to be thrown when the Amortization method is not configured
    """
    pass