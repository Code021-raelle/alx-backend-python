#!/usr/bin/env python3
"""
Contains a coroutine wait_random that waits for a random delat and returns it
"""
import asyncio
import random
from typing import Any


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0
    and max_delay and eventually returns it.

    Args:
        max_delay (int): Maximum delay in seconds (default is 10)

    Returns:
        float: The random delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
