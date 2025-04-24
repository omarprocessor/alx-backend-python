#!/usr/bin/env python3
"""Module that provides a function to create a multiplier function."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier."""
    def multiplier_function(n: float) -> float:
        return n * multiplier
    return multiplier_function
