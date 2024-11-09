#!/usr/bin/env python3
"""This module uses type annotations"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes str and int or float and returns a tuple"""
    return (k, v ** 2)
