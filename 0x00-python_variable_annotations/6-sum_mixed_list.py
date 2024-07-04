#!/usr/bin/env python3
"""
This module provides a function to sum a list of integers and floats
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and float numbers

    Args:
        mxd_lst (
        List[Union[int, float]]): The list of integers and floats to sum

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(mxd_lst)
