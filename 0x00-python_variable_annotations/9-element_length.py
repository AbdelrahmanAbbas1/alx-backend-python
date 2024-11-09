#!/usr/bin/env python3
"""This module uses type annotations"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """takes a list and returns the length of its items"""
    return [(i, len(i)) for i in lst]
