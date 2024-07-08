#!/usr/bin/env python3
"""
Contains a function task_wait_n that spawns task_wait_random n times
"""
import asyncio
from typing import List
from 3-tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the speciifed max_delay and returns
    the list of all the delays in ascending order.

    Args:
        n (int): Number of times to spawn task_wait_random
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
