#!/usr/bin/env python3
"""
Measure the average execution time of wait_n using n and max_delay.

This module provides a function to measure how long wait_n takes to run
and computes the average time per execution.
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n and return average time.

    Args:
        n (int): Number of times to spawn wait_n.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: Average execution time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return (total_time / n)
