#!/usr/bin/env python3
"""
a regular function take an integer and return asyncio.Task
"""
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    normal function that return asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
