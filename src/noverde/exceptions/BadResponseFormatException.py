from noverde.exceptions import NoverdeException

class BadResponseFormatException(NoverdeException):
    """Exception thrown when the response is not in a valid format"""
    pass