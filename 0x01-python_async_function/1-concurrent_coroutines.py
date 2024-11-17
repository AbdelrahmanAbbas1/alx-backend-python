#!/usr/bin/env python3
"""This module defines asynchronous function"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of floats"""
    tasks = [wait_random(max_delay) for i in range(n)]
    wait_times = await asyncio.gather(*tasks)
    return wait_times
