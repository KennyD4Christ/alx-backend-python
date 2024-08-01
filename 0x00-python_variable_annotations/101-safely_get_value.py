#!/usr/bin/env python3
"""
Module to Safely get a value from a dictionary by key, returning
a default value if the key is not present
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary by key, returning a default
    value if the key is not present.

    :param dct: The dictionary from which to get the value.
    :param key: The key whose value should be retrieved.
    :param default: The value to return if the key is not present
    in the dictionary.
    :return: The value associated with the key if it is present, otherwise
    the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
