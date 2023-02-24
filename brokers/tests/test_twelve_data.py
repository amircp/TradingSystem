import unittest
from datetime import datetime
from twelve_data import TwelveDataClient
from exceptions import NotSupportedAction

class TestTwelveDataClient(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TwelveDataClient()

    def test_get_data_csv(self):
        ticker = 'AAPL'
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2022, 1, 31)
        time_interval = '1day'
        output_format = 'csv'

        result = self.client.get_data(ticker,start_date,end_date,time_interval,output_format)

        self.assertIsInstance(result,str)