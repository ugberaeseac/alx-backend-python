#!/usr/bin/env python3
"""
type-annotated function
takes a string and an int OR float as arguments
returns a tuple.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    return a tuple
    """
    return (k, v**2)
