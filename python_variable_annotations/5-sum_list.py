#!/usr/bin/env python3
"""
this module contains a function which takes a list of floats
as argument and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    this function take a list of float as argument and
    sum each element into it list to return the result
    """
    result = 0
    for n in input_list:
        result += n
    return result
