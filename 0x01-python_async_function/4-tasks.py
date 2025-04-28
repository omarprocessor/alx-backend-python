#!/usr/bin/env python3
"""
Module that spawns multiple tasks using task_wait_random and gathers results.

This module defines a function that creates multiple asyncio tasks that wait
for a random amount of time and collects their completion times.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with a given max_delay and collect results.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay value for each task.

    Returns:
        List[float]: List of delays in order of task completion.
    """
    tasks = []
    delays = []

    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
