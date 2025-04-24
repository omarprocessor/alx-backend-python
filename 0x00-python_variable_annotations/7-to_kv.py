#!/usr/bin/env python3
"""Module that provides a function to return a tuple of a string and the square of a number."""


from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple containing a string k and the square of v as a float."""
    return (k, float(v ** 2))
