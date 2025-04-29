#!/usr/bin/env python3
"""
Module that measures the total runtime of executing
async_comprehension four times in parallel.
"""

import asyncio
import time
from typing import Callable
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times concurrently and
    returns the total time taken to execute all tasks.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
