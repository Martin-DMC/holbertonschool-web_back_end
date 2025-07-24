#!/usr/bin/env python3
"""
this module contain a function that concatenates
2 text and return only one string text
"""


def concat(str1: str, str2: str) -> str:
    """
    this function take 2 string text for return
    one sentence.
    on any other case, it function return a message on values error
    """
    if isinstance(str1, str) and\
            isinstance(str2, str):
        return str1 + str2
