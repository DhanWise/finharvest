"""
Module to download stock data from Yahoo Finance.
"""
import pandas as pd
import yfinance

from finharvest.datapoint import Datapoint, Parameter
from finharvest.exceptions import EmptyDataFrameException


def get_stock_data(stock_symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
    """Get stock data from Yahoo Finance."""
    data = yfinance.Ticker(stock_symbol).history(start=start_date, end=end_date)
    if data.empty:
        raise EmptyDataFrameException(f"Empty DataFrame for {stock_symbol}.")
    return data


class YahooFinanceStockData(Datapoint):
    description = "Get stock data from Yahoo Finance."

    parameters = [
        Parameter(
            name="stock_symbol",
            description="The stock symbol of the stock data.",
        ),
        Parameter(
            name="start_date",
            description="The start date of the stock data.",
        ),
        Parameter(
            name="end_date",
            description="The end date of the stock data.",
        ),
    ]

    def get_data(self, **kwargs: str) -> pd.DataFrame:
        _ = super().get_data(**kwargs)
        return get_stock_data(**kwargs)
