#!/usr/bin/env python3
"""
This module contains a function to sum a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and
        float numbers.

    Returns:
        float: The sum of the list of integers and floats.
    """
    return sum(mxd_lst)
