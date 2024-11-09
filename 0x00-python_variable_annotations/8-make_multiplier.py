#!/usr/bin/env python3
"""This module uses type annotations"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[float, float]:
    """takes float and returns a callable function"""
    return lambda x: multiplier * x
