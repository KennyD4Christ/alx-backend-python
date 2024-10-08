#!/usr/bin/env python3
"""
module to Measures the total execution time for wait_n(n, max_delay)
and returns the average time per coroutine.
"""
import asyncio
import time
import importlib

# Import wait_n from 1-concurrent_coroutines.py
module_name = "1-concurrent_coroutines"
wait_n = importlib.import_module(module_name).wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per coroutine.

    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: The average time per coroutine.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    total_time = end_time - start_time
    return total_time / n
