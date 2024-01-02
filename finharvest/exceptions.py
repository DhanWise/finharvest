class EmptyDataFrameException(Exception):
    """Raised when the DataFrame is empty."""

    def __init__(self, message="The DataFrame is empty."):
        super().__init__(message)
