#!/usr/bin/python3

"""
add function adds two integers a and b
if a or b is not integer it raise TypeError
add Function returns the addition of a and b
"""


def add_integer(a, b=98):
    """
    add two integers
    """

    if isinstance(a, int) is False and isinstance(a, float) is False:
        raise TypeError("a must be an integer")

    elif isinstance(b, int) is False and isinstance(b, float) is False:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
