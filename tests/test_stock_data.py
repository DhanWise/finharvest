from finharvest.data import fetch_data


def test_fetch_data_successful():
    fetch_data(
        "yf.stock_data",
        stock_symbol="AAPL",
        start_date="2023-12-01",
        end_date="2023-12-02",
    )
