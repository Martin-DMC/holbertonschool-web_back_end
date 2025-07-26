#!/usr/bin/env python3
"""
this module contains a function that take 2 parameters and
return a sort list of float numbers
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    this function take the first parameter as limit of elements
    to it list and take the second parameter as the max of deeley.
    after get it list use the algorithm bubble sort to return
    that list in ascendent order
    """
    lista = []
    i = 0
    while i < n:
        ping = wait_random(max_delay)
        lista.append(await ping)
        i += 1
    tmp = 0
    it = 0
    size = len(lista)

    while it < (size - 1):
        change = 0
        j = 0
        while j < (size - it - 1):
            if lista[j] > lista[j + 1]:
                tmp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = tmp
                change = 1
            j += 1
        if change == 0:
            break
        it += 1
    return lista
