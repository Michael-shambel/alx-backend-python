#!usr/bin/env python3
"""
function with itegers as argyments that measures the total execution time
return total_time / n
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    this function accept two argumet and return
    the time of execution
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed / n
