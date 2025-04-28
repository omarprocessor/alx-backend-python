#!/usr/bin/env python3
"""This module uses random to return delay in an async func."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits asynchronously for a random delay and returns it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
