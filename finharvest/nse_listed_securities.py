from typing import List

import os.path as op
import pathlib as pl
import tempfile

import pandas as pd
import requests

from .constants import REQUEST_HEADERS

tmp_dir = pl.Path(tempfile.gettempdir())
tmp_dir.mkdir(parents=True, exist_ok=True)
CACHED_DATA = tmp_dir / pl.Path("nse_listed_securities.pkl")


def _clean_up_downloaded_data(content: str) -> List[List[str]]:
    """Clean up the downloaded from NSE website for list of available equities"""

    all_rows_raw = content.split("\n")
    all_rows = list()
    for _row in all_rows_raw:
        if _row == "":
            continue
        all_rows.append([_value.strip() for _value in _row.split(",")])
    return all_rows


def _download_all_listed_securities():
    """Download all listed equities from NSE website and returns a pandas dataframe"""

    global REQUETS_HEADERS
    equities_download_url = (
        "https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv"
    )
    resp = requests.get(equities_download_url, headers=REQUEST_HEADERS)
    resp.raise_for_status()
    cleaned_data = _clean_up_downloaded_data(resp.text)
    cleaned_data_frame = pd.DataFrame(data=cleaned_data[1:], columns=cleaned_data[0])
    return cleaned_data_frame


def get_all_listed_securities():
    """
    Get all listed equities from NSE website as pandas dataframe.
    The dataframe contains the following columns:
        - SYMBOL
        - NAME OF COMPANY
        - SERIES
        - DATE OF LISTING
        - PAID UP VALUE
        - MARKET LOT
        - ISIN NUMBER
        - FACE VALUE
    """

    global CACHED_DATA
    if op.exists(CACHED_DATA):
        return pd.read_pickle(CACHED_DATA)
    else:
        df = _download_all_listed_securities()
        df.to_pickle(CACHED_DATA)
        return df
