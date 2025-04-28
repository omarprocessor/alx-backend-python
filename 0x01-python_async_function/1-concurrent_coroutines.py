import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random



async def wait_n(n:int, max_delay:int) -> List:
    task = [wait_random() for i in range(max_delay)]
    delay = await asyncio.gather(*task)

    return sorted(delay)