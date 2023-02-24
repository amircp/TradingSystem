"""Base class to define the interfaces to support our broker integrations"""
import os
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

    @staticmethod
    def get_api_secret(secret_name):
        """This method will read from a secure storage the credentials,keys or secret to establish a
        connection with the broker
         Get API secret from environment variable
         :param api_secret_name: name of the environment variable
         :return: The API secret
         """
        api_secret = os.getenv(secret_name, default=None)
        if api_secret is None:
            raise ValueError(f"API secret {secret_name} not found")
        else:
            return api_secret

