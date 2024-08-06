#!/usr/bin/env python3
"""
0-async_generator.py

This module contains the async_generator coroutine.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that asynchronously yields a random number between 0 and 10,
    after waiting for 1 second, 10 times.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
