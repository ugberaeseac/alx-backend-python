#!/usr/bin/env python3
"""
async coroutine that spawns
a function multiple times at the same time
Returns a list of all the delays in ascending order
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns task_wait_random n times
    return the list of delays in
    ascending order
    """
    async_tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*async_tasks)
    return sorted(delays)
