#!/usr/bin/env python3
"""
this module contain a function which take as parameter a
list of iterable elements and return a list with those elements
and your length
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    this function take the list of iterable elements
    and count the length of each element into these list.
    to after return a list of tuples with the element in
    yourself and the number of your length
    """
    return [(i, len(i)) for i in lst]
