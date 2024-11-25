#!/usr/bin/python3
"""Addition module
This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """Add two integers or floats and return their sum.

    Args:
        a: The first number (integer or float).
        b: The second number (integer or float, default is 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
