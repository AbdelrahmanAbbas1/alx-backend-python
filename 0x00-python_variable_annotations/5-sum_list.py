#!/usr/bin/env python3
"""This module defines function with ytpe annotation"""


def sum_list(input_list: list[float]) -> float:
    sum: float = 0
    for i in input_list:
        sum = sum + i
    return sum
