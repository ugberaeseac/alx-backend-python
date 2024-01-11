#!/usr/bin/env python3
"""
type-annotated function
takes a list of floats as argument
returns their sum as a float.
"""


def sum_list(input_list: list[float]) -> float:
    """
    returns sum
    """
    Total = 0.00
    for input in input_list:
        Total += input
    return Total
