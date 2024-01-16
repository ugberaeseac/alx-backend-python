#!/usr/bin/env python3
"""
Async generator - coroutine loops 10times
asynchronously wait a second then yield a random
number between 0 and 10.
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    loop, asynchronously wait 1 sec and
    yield a random number
    """
    for _ in range(10):
        number = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield number
