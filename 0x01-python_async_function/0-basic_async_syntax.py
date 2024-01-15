#!/usr/bin/env python3
"""
An asynchronous coroutine that waits for a random delay
between 0 and max_delay (inclusive)
Returns the random float value representing the delay.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    async coroutine waits for random delay
    returns delay
    """
    delay = random.uniform(0, max_delay + 1)
    await asyncio.sleep(delay)
    return delay
