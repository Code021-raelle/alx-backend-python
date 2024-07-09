#!/usr/bin/env python3
"""
Module: 1-async_comprehension
"""

import asyncio
from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over asy_generator, then returns the 10 random numbers.
    """
    return [i async for i in async_generator()]
