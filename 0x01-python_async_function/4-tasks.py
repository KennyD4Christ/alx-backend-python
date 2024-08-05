#!/usr/bin/env python3
"""
module to Spawns task_wait_random n times with the specified max_delay
"""
import asyncio
from typing import List
import importlib

# Import task_wait_random from 3-tasks.py
module_name = "3-tasks"
task_wait_random = importlib.import_module(module_name).task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.

    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        List[float]: List of all delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    sorted_delays = []
    while delays:
        min_delay = min(delays)
        sorted_delays.append(min_delay)
        delays.remove(min_delay)

    return sorted_delays
