#!/usr/bin/env python3
"""
measures the total execution time for a coroutine
returns run time / n -> float
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the runtime
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter() - start_time
    return end_time / n
