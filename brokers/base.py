"""Base class to define the interfaces to support our broker integrations"""
from abc import ABC, abstractmethod

class BrokerAPI(ABC):
    """Base class to define the interfaces to support our broker integrations"""
    @abstractmethod
    def open_position(self):
        pass

    @abstractmethod
    def close_position(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def get_api_secret(self):
        """This method will read from a secure storage the credentials,keys or secret to establish a
        connection with the broker"""
        pass

