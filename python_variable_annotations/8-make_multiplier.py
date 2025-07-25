#!/usr/bin/env python3
"""
this module contains a function that takes a
float multiplier as argument and returns a function that
multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    this function take a float number as parameter and use
    that number as multiplier for the function that return
    """
    def resultado(num: float) -> float:
        """
        this function take a float number and return the 
        result between that number and the previous multiplier"""
        return num * multiplier
    return resultado
