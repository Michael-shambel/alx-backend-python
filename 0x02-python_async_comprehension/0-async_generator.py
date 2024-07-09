#!/usr/bin/env python3
"""
function coroutine take no argumets. 10 times
"""
import asyncio
import random
from typing import List


async def async_generator() -> List[float]: # type: ignore
    """
    function that loop ten times and wait 1 second
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
