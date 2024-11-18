#!/usr/bin/env python3
"""This module defines an async function"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields a random number every 1 second"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
