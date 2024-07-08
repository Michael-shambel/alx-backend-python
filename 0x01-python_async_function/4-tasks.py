#!/usr/bin/env python3
"""
async functionroutine that takes two argument and return
the list of all the delays
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    take two arument and retunn the list of delay
    """
    list_delay = []
    for _ in range(n):
        delay = task_wait_random(max_delay)
        list_delay.append(delay)
    delays = await asyncio.gather(*list_delay)

    return sorted(delays)
