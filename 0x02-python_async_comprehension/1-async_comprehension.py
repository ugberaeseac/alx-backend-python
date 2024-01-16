#!/usr/bin/env python3
"""
async comprehension
import async_generator from 0-async_generator
returns list of 10 random numbers using
async comprehension
"""


from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
    return 10 random numbers using async comprehension
    """
    random_numbers = [number async for number in async_generator()]
    return random_numbers
