#!/usr/bin/env python3
"""
2-measure_runtime.py

This module contains the measure_runtime coroutine.
"""

import asyncio
import time
import importlib

importlib_module = importlib.import_module(
    '1-async_comprehension'
)
async_comprehension = importlib_module.async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing async_comprehension
    four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time
