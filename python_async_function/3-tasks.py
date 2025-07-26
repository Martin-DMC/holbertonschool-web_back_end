#!/usr/bin/env python3
"""
this module contains a function which return a task object
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """
    this function receive a parameter to after call
    a the function wait_random with that parameter,
    and create a task to after return it
    """
    tarea = asyncio.create_task(wait_random(max_delay))
    return tarea
