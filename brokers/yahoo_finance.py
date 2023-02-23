import yfinance
from base import BrokerAPI
from exceptions import NotSupportedAction

class YahooFinanceClient(BrokerAPI):
    """This class is only for data extraction from Yahoo Finance"""
    def get_data(self,ticker, start_date, end_date, time_interval,output_format='csv'):
        """
        Extract data from Yahoo Finance. This method rely on a third party library called yfinance.
        :param ticker: Instrument dymbol
        :param start_date: Start Date
        :param end_date: End Date
        :param time_interval:Supported Intervals Formats(1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)
        :param output_format: Supported csv,sql,json,dict,string,pandas(dataframe)
        :return: Default Instrument data in CSV format
        """
        # make a GET request to the YahooFinance API endpoint for the specified ticker and time interval
        try:
            response = yfinance.Ticker(ticker).history(start=start_date, end=end_date, interval=time_interval)
        except Exception as exception:
            raise

        if output_format == 'csv':
            return response.to_csv()
        elif output_format == 'sql':
            return response.to_sql()
        elif output_format == 'json':
            return response.to_json()
        elif output_format == 'dict':
            return response.to_dict()
        elif output_format == 'pandas':
            return response
        else:
            raise ValueError(f'Unsupported output format: {output_format}')


    def get_api_secret(self):
        """This method will read from a secure storage the credentials,key or secret to establish a
        connection with the broker"""
        raise NotSupportedAction("Yahoo Finance does not support this action")
        pass

    def open_position(self):
        raise NotSupportedAction("Yahoo Finance does not support this action")

    def close_position(self):
        raise NotSupportedAction("Yahoo Finance does not support this action")

if __name__  == '__main__':
    print(YahooFinanceClient().get_data('AAPL','2021-01-01','2021-01-31','1d'))