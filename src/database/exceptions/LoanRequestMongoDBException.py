from database.exceptions import LoanRequestDBException


class LoanRequestMongoDBException(LoanRequestDBException):
    """
    A generic exception to be thrown when problems occur 
    in the LoanRequestMongoDB
    """
    pass
