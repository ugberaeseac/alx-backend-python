#!/usr/bin/env python3
"""
type-annotated function
takes a list of floats as argument
returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    returns sum
    """
    Total = 0.00
    for input in input_list:
        Total += input
    return Total
