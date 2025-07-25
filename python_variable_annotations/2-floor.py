#!/usr/bin/env python3
"""
this module contains a function that round a
float to the less int number
"""
import math


def floor(n: float) -> int:
    """
    this function take as parameter a float and to convert a int.
    on any other case, her return a message  with 'invalid number type'
    """
    if not isinstance(n, float):
        return ('invalid number type')
    return int(n)
