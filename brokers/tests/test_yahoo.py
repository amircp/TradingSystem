import unittest
from datetime import datetime
from yahoo_finance import YahooFinanceClient
from exceptions import NotSupportedAction

class TestYahooFinanceClient(unittest.TestCase):
    def setUp(self):
        self.client = YahooFinanceClient()

    def test_get_data_returns_csv(self):
        ticker = 'AAPL'
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2022, 1, 31)
        time_interval = '1d'
        output_format = 'csv'

        result = self.client.get_data(ticker, start_date, end_date, time_interval, output_format)

        self.assertIsInstance(result, str)

    def test_get_data_returns_sql(self):
        ticker = 'AAPL'
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2022, 1, 31)
        time_interval = '1d'
        output_format = 'sql'

        result = self.client.get_data(ticker, start_date, end_date, time_interval, output_format)

        #Todo assert?
    # To-Do
    #Add more unit test to validate the rest of the output formats

    def test_get_data_raises_error_for_invalid_output_format(self):
        ticker = 'AAPL'
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2022, 1, 31)
        time_interval = '1d'
        output_format = 'invalid'

        with self.assertRaises(ValueError):
            self.client.get_data(ticker, start_date, end_date, time_interval, output_format)

    def test_get_api_secret_raises_not_supported_action(self):
        with self.assertRaises(NotSupportedAction):
            self.client.get_api_secret()

    def test_open_position_raises_not_supported_action(self):
        with self.assertRaises(NotSupportedAction):
            self.client.open_position()

    def test_close_position_raises_not_supported_action(self):
        with self.assertRaises(NotSupportedAction):
            self.client.close_position()

if __name__ == '__main__':
    unittest.main()
