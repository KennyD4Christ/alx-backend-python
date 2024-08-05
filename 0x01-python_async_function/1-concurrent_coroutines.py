#!/usr/bin/env python3
"""
module to spawns wait_random n times with the specified max_delay.
"""
import asyncio
from typing import List
import importlib

# Import wait_random from 0-basic_async_syntax.py
module_name = "0-basic_async_syntax"
wait_random = importlib.import_module(module_name).wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of all delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    sorted_delays = []
    while delays:
        min_delay = min(delays)
        sorted_delays.append(min_delay)
        delays.remove(min_delay)

    return sorted_delays
