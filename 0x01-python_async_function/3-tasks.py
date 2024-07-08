#!/usr/bin/env python3
"""
Contains a function task_wait_random that returns an asyncio.Task.\
"""
import asyncio
from typing import Any
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task that waits
    for a random delay.

    Args:
        max_delay (int): Maximum delay in seconds

    Returns:
        asyncio.Task: A task that waits for a random delay.
    """
    return asyncio.create_task(wait_random(max_delay))
