#!/usr/bin/env python3
"""
this module contains a function that take 2 parameters and
return a sort list of float numbers
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    this function take the first parameter as limit of elements
    to it list and take the second parameter as the max of deeley.
    and after put in each element in order of finish
    """
    lista = [task_wait_random(max_delay) for _ in range(n)]
    lista_en_orden = []

    for completas in asyncio.as_completed(lista):
        delay = await completas
        lista_en_orden.append(delay)
    return lista_en_orden
