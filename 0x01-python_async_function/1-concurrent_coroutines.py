#!/usr/bin/env python3
"""This module contains a function that 
runs multiple asynchronous delays concurrently.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with max_delay and 
    returns the list of all delays sorted in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return (sorted(delays))
