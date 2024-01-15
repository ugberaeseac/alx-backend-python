#!/usr/bin/env python3
"""
Asynchronous coroutine that spawans
multiple coroutines at the same time
Returns a list of all the delays in ascending order
"""


import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    execute wait_random - n times
    return the list of delays in
    ascending order using sorted()
    """
    async_tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*async_tasks)
    return sorted(delays)
