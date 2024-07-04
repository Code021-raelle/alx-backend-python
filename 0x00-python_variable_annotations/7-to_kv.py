#!/usr/bin/env python3
"""
This module provides a function that takes a string and an int ot float
and returns a tuple
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the string `k`
    and the second element is the square of `v`.

    Args:
        k (str): The string
        v (Union[int, float]): The value to be squared

    Returns:
        Tuple[str, float]: A tuple containing the string and the square
        of the value.
    """
    return (k, float(v ** 2))
