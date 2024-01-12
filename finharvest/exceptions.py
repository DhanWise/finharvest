"""
Module defining all the exception classes for the package.
"""


class InvalidDatapointException(Exception):
    """Raised when the datapoint is not present in the catalog."""

    def __init__(self, name):
        super().__init__(f"The datapoint {name} is not present in the catalog.")


class EmptyDataFrameException(Exception):
    """Raised when the DataFrame is empty."""

    def __init__(self, message="The DataFrame is empty."):
        super().__init__(message)
