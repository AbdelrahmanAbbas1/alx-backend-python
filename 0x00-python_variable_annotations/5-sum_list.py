#!/usr/bin/env python3
"""This module defines function with ytpe annotation"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    sum: float = 0
    for i in input_list:
        sum = sum + i
    return sum
