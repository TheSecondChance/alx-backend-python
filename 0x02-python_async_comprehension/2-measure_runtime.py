#!/usr/bin/env python3
"""
parallel comprehensions async
"""

import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """async measure_runtime"""
    start = asyncio.get_running_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    itEnd = asyncio.get_running_loop().time()
    return itEnd - start
