#!/usr/bin/env python3
"""This module defines asynchronous function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Takes integer and return a random float"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
