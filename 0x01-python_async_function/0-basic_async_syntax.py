#!/usr/bin/env python3
"""
module to Waits for a random delay between 0 and max_delay
(included and float value) seconds
and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay
    (included and float value) seconds
    and eventually returns it.

    Args:
        max_delay (int): Maximum delay in seconds.
        Default is 10 seconds.

    Returns:
        float: The random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
