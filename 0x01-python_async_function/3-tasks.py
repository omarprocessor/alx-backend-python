#!/usr/bin/env python3
"""
Module for creating asyncio tasks that execute a random wait.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio Task from the wait_random coroutine and return it.
    Args:
        max_delay (int): The maximum delay to pass to wait_random.Returns:
        asyncio.Task: The asyncio Task created from wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
