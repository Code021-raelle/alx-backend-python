#!/usr/bin/env python3
"""
This module provides a function to zoom into an array by a given factor
"""

from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Returns a list with elements of the tuple repeated by the factor

    Args:
        lst (Tuple[int, ...]): The input tuple
        factor (int, optional): The repetition factor. Defaults to 2.

    Returns:
        List[int]: The zoomed-in list
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
