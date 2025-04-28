#!/usr/bin/env python3
import asyncio
import random

"""This module uses random to return delay in an async func."""

async def wait_random(max_delay: int = 10) -> float:
    """Returns random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
