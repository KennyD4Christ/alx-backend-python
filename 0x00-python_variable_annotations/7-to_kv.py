#!/usr/bin/env python3
"""
This module contains a function to return a tuple with a string and the square of an int/float.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple with a string and the square of an int/float.

    Args:
        k (str): The string key.
        v (Union[int, float]): The int or float value.

    Returns:
        Tuple[str, float]: A tuple where the first element is k and the second element is the square of v.
    """
    return (k, float(v ** 2))
