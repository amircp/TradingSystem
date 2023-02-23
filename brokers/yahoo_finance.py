from base import BrokerAPI
from exceptions import NotSupportedAction

class YahooFinanceClient(BrokerAPI):
    """This class is only for data extraction from Yahoo Finance"""
    def get_data(self):
        pass

    def get_api_secret(self):
        pass

    def open_position(self):
        raise NotSupportedAction("Yahoo Finance does not support this action")

    def close_position(self):
        raise NotSupportedAction("Yahoo Finance does not support this action")

