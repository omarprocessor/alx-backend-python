#!/usr/bin/env python3
"""
This module defines a coroutine that measures the total runtime
of executing four instances of the async_comprehension coroutine concurrently.
"""

import asyncio
import time
from importlib import import_module as import_mod

async_comprehension = import_mod('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the time taken to run four instances of async_comprehension.
    Returns:
        float: The total runtime in seconds.
    """
    start: float = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end: float = time.time()
    return end - start
