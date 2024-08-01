#!/usr/bin/env python3
"""
This module contains a function that zooms in on an array by repeating its elements.
"""

from typing import List, Tuple

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zoom in on a tuple by repeating each element a number of times specified by factor.

    Args:
        lst (Tuple[int, ...]): A tuple of integers to zoom in on.
        factor (int, optional): The number of times to repeat each element. Defaults to 2.

    Returns:
        List[int]: A list containing each element of the tuple repeated factor times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

# Example usage
array = (12, 72, 91)  # Changed to tuple to match the function type

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Ensure factor is an integer
