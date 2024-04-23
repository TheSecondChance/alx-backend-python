#!/usr/bin/env python3
"""
coroutine called async_generator no argument taken
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async_generator wait one second each"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
