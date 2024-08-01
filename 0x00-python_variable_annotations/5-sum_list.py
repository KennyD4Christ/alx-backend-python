#!/usr/bin/env python3
"""
This module contains a function to sum a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum a list of floats.

    Args:
        input_list (List[float]): The list of float numbers.

    Returns:
        float: The sum of the list of floats.
    """
    return sum(input_list)
