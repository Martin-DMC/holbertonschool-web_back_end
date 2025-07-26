#!/usr/bin/env python3
"""
this module contains a function asynchronous
which return a random number
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    this function return a float number between 0 until the value get.
    if nothing value it function use 10 as max deeley
    """
    await asyncio.sleep(1)
    return random.uniform(0, max_delay)
