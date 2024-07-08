#!/usr/bin/env python3
"""
asynchronous coroutine that takes in aninteger argumet with default value
and return it after some delay bitween 0 and max_delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    async random sleep function
    """
    i = random.randint(0, max_delay)
    await asyncio.sleep(i)
    return i
