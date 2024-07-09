#!/usr/bin/env python3
"""
Module: 2-measure_runtime
"""
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather and measures the total runtime.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
