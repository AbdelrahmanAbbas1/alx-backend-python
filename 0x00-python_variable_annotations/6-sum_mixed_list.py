#!/usr/bin/env python3
""" A type-annotated function."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function sum_mixed_list which takes
    a list mxd_lst of integers and floats
    and returns their sum as a float."""
    return float(sum(mxd_lst))
