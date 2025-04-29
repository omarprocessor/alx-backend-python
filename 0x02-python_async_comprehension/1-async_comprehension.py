#!/usr/bin/env python3
"""
Module that contains a coroutine to collect random numbers
from an asynchronous generator using async comprehension.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random float values from async_generator using
    async comprehension and returns them as a list.
    """
    return [i async for i in async_generator()]
