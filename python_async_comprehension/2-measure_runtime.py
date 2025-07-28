#!/usr/bin/env python3
"""
this module contains a function
which calculate an estimate of total run time
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    this function starting the time for after to do a loop
    and make a list of task. then use this list for asyncio.gather
    to await you finishes and can calculate the time.
    """
    time_inicial = time.time()
    lista_tareas = []
    for _ in range(0, 4):
        task = asyncio.Task(async_comprehension())
        lista_tareas.append(task)
    await asyncio.gather(*lista_tareas)
    time_final = time.time()

    duracion = (time_final - time_inicial)
    return duracion
