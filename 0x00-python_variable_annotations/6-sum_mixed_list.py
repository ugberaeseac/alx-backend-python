#!/usr/bin/env python3
"""
type-annotated function
takes a mixed list of integers and floats as argument
returns their sum as a float.
"""


from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    returns sum
    """
    Total = 0
    for input in mxd_lst:
        Total += input
    return Total
