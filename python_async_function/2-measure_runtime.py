#!/usr/bin/env python3
"""
this module contains a function which calculate a
the total execution time and return the estimate value
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    this function take 2 parameters to call a wait_n function and
    calculate the total execute time.
    return the value estimate for each run
    """
    time_inicial = time.time()
    asyncio.run(wait_n(n, max_delay))
    time_final = time.time()

    duracion = (time_final - time_inicial) / n
    return duracion
