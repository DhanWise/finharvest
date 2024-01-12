"""
This module would work as the main touchpoint for other packages or the applications to access
the data
"""
from typing import Any

import pandas as pd

from finharvest.catalog import all_datapoints
from finharvest.exceptions import InvalidDatapointException


def _initialize_loader(module_name: str, class_name: str) -> Any:
    """Initialize the data loader class"""
    module = __import__("finharvest." + module_name, globals(), locals(), [class_name])
    return getattr(module, class_name)


def fetch_data(datapoint: str, **kwargs: str) -> pd.DataFrame:
    """
    Fetch the data from the datapoint
    """
    # check if the datapoint is present in the catalog
    if datapoint not in all_datapoints:
        raise InvalidDatapointException(datapoint)

    # loads the module lazily when needed.
    data_loader = _initialize_loader(
        all_datapoints[datapoint][0], all_datapoints[datapoint][1]
    )(datapoint)
    # pass the function call to the datapoint class referenced by the datapoint
    return data_loader.get_data(**kwargs)
