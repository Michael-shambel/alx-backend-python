#!/usr/bin/env python3
"""
async functionroutine that takes two argument and return
the list of all the delays
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    take two arument and retunn the list of delay
    """
    list_delay = []
    for _ in range(n):
        delay = wait_random(max_delay)
        list_delay.append(delay)
    delays = await asyncio.gather(*list_delay)

    return sorted(delays)
