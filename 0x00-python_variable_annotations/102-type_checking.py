#!/usr/bin/env python3
"""
Module to Zoom in on the array by repeating each element a specified
number of times
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom in on the array by repeating each element a specified
    number of times.

    :param lst: The list of integers to zoom in on.
    :param factor: The factor by which to repeat each element.
     Defaults to 2.
    :return: A new list where each element of the original list is
     repeated 'factor' times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
