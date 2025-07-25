#!/usr/bin/env python3
"""
this module contains a function which takes a list
of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    this function take a mixed list and sum all elements which
    it contain to return his float result of sum
    """
    result = 0
    for n in mxd_lst:
        result += n
    return float(result)
