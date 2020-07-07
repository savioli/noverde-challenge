from database.exceptions import LoanRequestDBException


class LoanRequestDynamoDBException(LoanRequestDBException):
    """
    A generic exception to be thrown when problems occur 
    in the DynamoDB
    """
    pass
