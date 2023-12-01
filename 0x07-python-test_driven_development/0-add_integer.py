#!/usr/bin/python3
"""
This is the 0-add_integer module.
It contains a function for adding two integers or floats.

"""


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
