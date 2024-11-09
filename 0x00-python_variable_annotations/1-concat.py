#!/usr/bin/env python3
"""This module defines a function with type annotaions"""


def concat(str1: str, str2: str) -> str:
    "Takes two strings and return them concatenated"
    return "{}{}".format(str1, str2)
