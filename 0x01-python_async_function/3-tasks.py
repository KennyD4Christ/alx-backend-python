#!/usr/bin/env python3
import asyncio
import importlib

# Import wait_random from 0-basic_async_syntax.py
module_name = "0-basic_async_syntax"
wait_random = importlib.import_module(module_name).wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for wait_random with the given max_delay.
    
    Args:
        max_delay (int): Maximum delay for wait_random.
    
    Returns:
        asyncio.Task: The created task.
    """
    return asyncio.create_task(wait_random(max_delay))
