#!/usr/bin/env python3
"""
This module provides a function to safely get a value from a dicitonary
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[
            T, None] = None) -> Union[Any, T]:
    """
    Returns the value from the dictionary if the key exists,
    otherwise returns the default value

    Args:
        dct (Mapping[Any, Any]): The dictionary to search
        key (Any): The key to look for in the dictionary
        default (Union[T, None]): The default value to return if the key
        is not found.

    Returns:
        Union[Any, T]: The value associated with the key, or the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
