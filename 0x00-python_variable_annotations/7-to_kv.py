#!/usr/bin/env python
"""This module uses type annotations"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int | float]) -> Tuple[str, float]:
    return (k, v)
