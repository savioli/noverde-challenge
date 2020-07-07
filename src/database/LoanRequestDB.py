from abc import ABC, abstractmethod


class LoanRequestDB(ABC):
    """Provides an interface to persist a LoanRequest"""

    @abstractmethod
    def save_loan_request(self, loan_request):
        """Saves a LoanRequest"""
        pass

    @abstractmethod
    def update_loan_request(self, uuid):
        """Updates a LoanRequest"""
        pass

    @abstractmethod
    def get_loan_request_by_uuid(self, uuid):
        """Gets a LoanRequest by uuid"""
        pass

    @abstractmethod
    def to_loan_request(self, record):
        """Transforms a record in a LoanRequest"""
        pass
