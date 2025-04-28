#!/usr/bin/env python3

"""
Module for creating asyncio tasks that run multiple random waits.

This module contains the `task_wait_n` function that takes in two arguments:
`n` (the number of tasks to run) and `max_delay` (the maximum delay for
each random wait). It returns a list of floating-point numbers, each
representing the delay of a task, in the order they completed.
"""

import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """
    Run `n` tasks that each wait for a random delay up to `max_delay`.

    Args:
        n (int): The number of tasks to run.
        max_delay (int): The maximum delay for each task.

    Returns:
        list: A list of floats representing the delays each task took.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return results
