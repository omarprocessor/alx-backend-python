#!/usr/bin/env python3
"""Module function to safely get a value from a dictionary."""


from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Return value associated with 'key' in 'dct' if it exists, else return 'default'."""
    if key in dct:
        return dct[key]
    else:
        return default
