import pandas as pd
import yfinance

from .exceptions import EmptyDataFrameException


def get_stock_data(stock_symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
    """Get stock data from Yahoo Finance."""
    data = yfinance.Ticker(stock_symbol).history(start=start_date, end=end_date)
    if data.empty:
        raise EmptyDataFrameException(f"Empty DataFrame for {stock_symbol}.")
    return data
