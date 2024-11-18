#!/usr/bin/env python3
"""This module defines asynchronous function"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of floats"""
    tasks = [task_wait_random(max_delay) for i in range(n)]
    wait_times = await asyncio.gather(*tasks)
    return sorted(wait_times)
