"""
This module defines the common interface to all datapoints.
"""

from typing import List

from abc import ABC
from dataclasses import dataclass


@dataclass
class Parameter:
    name: str
    description: str


class Datapoint(ABC):
    """
    The common interface to all datapoints.
    """

    parameters: List[Parameter] = []
    description: str

    def __init__(self, datapoint: str):
        self.datapoint = datapoint

    def get_data(self, **kwargs):
        self._validate_input_arguments(**kwargs)
        pass

    def get_parameters(self):
        return self.parameters

    def _validate_input_arguments(self, **kwargs):
        pass
