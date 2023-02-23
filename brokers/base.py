"""Base class to define the interfaces to support our broker integrations"""
from abc import ABCMeta, abstractmethod

class BrokerAPI(ABCMeta):
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
        pass

