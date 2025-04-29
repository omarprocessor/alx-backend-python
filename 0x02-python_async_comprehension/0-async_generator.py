#!/usr/bin/env python3
"""
Creates an asynchronous generator that yields random numbers.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously yields a random float between 0 and 10, one at a time,
    with a 1-second delay between each yield. Repeats this process 10 times.
    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
