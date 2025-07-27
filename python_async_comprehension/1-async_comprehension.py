#!/usr/bin/env python3
"""
this module contains a function which collects 10 random numbers
and after return a list with it numbers
"""
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    this function is responsible for calling the number generator for after
    to collect your numbers on a list and can return that.

    but it function collect all nambers using an
    **asynchronous list comprehension**
    """
    result = [i async for i in async_generator()]
    return result
