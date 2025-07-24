#!/usr/bin/env python3
"""
this module contain a function to add numbers of type float,
and the value of return  also float
"""


def add(a: float, b: float) -> float:
    """
    this function only take 2 numbers of type float
    to return the value of add those numbers.
    on any other case, it function return a message on values error
    """
    if isinstance(a, float) and\
            isinstance(b, float):
        return float(a + b)
    else:
        print('valores incorrectos')
