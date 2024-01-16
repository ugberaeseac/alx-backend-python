#!/usr/bin/env python3
"""
Run-time for four paallel async comprehensions
executes async_comprehension four times
returns total run-time
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times
    Measure and return the total run-time
    """
    async_tasks = [async_comprehension() for _ in range(4)]
    start_time = time.perf_counter()
    await asyncio.gather(*async_tasks)
    end_time = time.perf_counter() - start_time
    return end_time
