#!/usr/bin/env python3
"""
This module contains a function that returns a tuple of two integers:
a start index and an end index. These indices correspond to the correct
range of items to be returned from a list for specific pagination parameters.
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    this function take the parameter page and with that calculate the
    index, depending of the number of page this function calculate
    the start and the end value to after return these data on a tuple

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple of two integers containing the start index
                and end index.
    """
    if page == 1:
        inicio = 0
    elif page == 2:
        inicio = page_size
    elif page == 3:
        inicio = page_size * 2
    else:
        inicio = page_size * (page - 1)

    fin = inicio + page_size
    return (inicio, fin)
