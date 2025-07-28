#!/usr/bin/env python3
"""
this module contain a coroutine called async_generator
that takes no arguments.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None]:
    """
    This function is an asynchronous generator.
    Generates 10 random numbers between 0 and 10,
    waiting 1 second between each one.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        delay = random.uniform(0, 10)
        yield delay
