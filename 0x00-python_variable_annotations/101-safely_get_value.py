#!/usr/bin/env python3
"""
This module contains a function that safely retrieves a value
from a dictionary.
"""

from typing import Mapping, Any, Union, TypeVar

# Define a type variable that can be any type
T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Union[T, None] = None) -> Union[T, None]:
    """
    Safely get a value from a dictionary.

    Args:
        dct (Mapping[Any, T]): A dictionary where the keys are of any type and
        values are of type T.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None], optional): The default value to return if
        the key is not found. Defaults to None.

    Returns:
        Union[T, None]: The value associated with the key if it exists,
        otherwise the default value or None.
    """
    if key in dct:
        return dct[key]
    else:
        return default
