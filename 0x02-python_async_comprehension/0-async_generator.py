#!/usr/bin/env python3
"""This module defines an async function"""
import asyncio
import random


async def async_generator():
    """Yields a random number every 1 second"""
    for i in range(10):
        yield random.uniform(0, 10)
