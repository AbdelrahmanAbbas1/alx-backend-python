#!/usr/bin/env python3
"""This module defines not an async function"""
import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """A function that returns a taks function"""
    return asyncio.create_task(wait_random(max_delay))
