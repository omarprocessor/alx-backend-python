#!/usr/bin/env python3
"""This module measures the total
 time taken by wait_n function.
"""
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measures the time taken by wait_n and returns
    the average time per execution."""
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
