import os
from base import BrokerAPI
from exceptions import NotSupportedAction
from twelvedata import TDClient #https://github.com/twelvedata/twelvedata-python

class TwelveDataClient(BrokerAPI):
    """This class is only for data extraction from TwelveData"""

    def __init__(self):
        self.api_key = super().get_api_secret("TWELVE_API_KEY")

    def get_data(self, ticker, start_date, end_date, time_interval, output_format="csv"):
        """
        Extract data from 12Data API. This method rely on a third party library called twelvedata.
        :param ticker: Instrument Symbol
        :param start_date: Start Date
        :param end_date: End Date
        :param time_interval: Support Intervals Formats(1min, 5min, 15min, 30min, 45min, 1h, 2h, 4h, 8h, 1day, 1week, 1month)
        :param output_format: Support csv,json,pandas(dataframe)
        :return: Default Instrument data in CSV format
        """
        # make a GET request to the TwelveData API endpoint for the specified ticker and time interval
        try:
            client = TDClient(apikey=self.api_key)
            response = client.time_series(symbol=ticker, interval=time_interval, start_date=start_date,
                                          end_date=end_date)
        except Exception as e:
            raise e

        if output_format == 'csv':
            return response.as_csv()
        elif output_format == 'json':
            return response.as_json()
        elif output_format == 'pandas':
            return response.as_pandas()
        else:
            raise ValueError(f'Unsupported output format: {output_format}')


    def open_position(self):
        raise NotSupportedAction("Yahoo Finance does not support this action")

    def close_position(self):
        raise NotSupportedAction("Yahoo Finance does not support this action")

if __name__ == "__main__":
    client = TwelveDataClient().get_data('AAPL','2022-01-01','2022-02-01','1day')
    print(client)