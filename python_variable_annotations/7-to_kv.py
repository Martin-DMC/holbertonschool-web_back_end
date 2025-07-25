#!/usr/bin/env python3
"""
this module contains a fuction hat takes a string k and an
int OR float v as arguments and returns a tuple. The first
element of the tuple is the string k. The second element is
the square of the int/float v and should be annotated as a float
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    this function take 2 parameters.

    param k: str
    param v: could be int or float

    return: a tuple with the str as first element and
            as second element the square of the int/float
    """
    if k and v:
        v = v * v
        retorno = (k, v)
    return retorno
