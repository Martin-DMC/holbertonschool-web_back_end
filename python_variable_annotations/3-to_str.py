#!/usr/bin/env python3
"""
this module contains a function that takes a float n
as argument and returns the string representation of the float
"""


def to_str(n: float) -> str:
    """
    this function take as parameter a float number and convert to
    the his representation on text.
    on any other case, it function return a message on values error
    """
    if isinstance(n, float):
        return str(n)
    return print('invalid argument type')
