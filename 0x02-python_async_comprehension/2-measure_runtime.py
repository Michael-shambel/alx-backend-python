#!/usr/bin/env python3
"""
write a measure_runtime coroutine that will execute async_comprehension
 four times in parallel using asyncio.gather.
"""
import asyncio
import time
import random
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    write a measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.
    """
    st = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    ed = time.perf_counter()
    return ed - st
