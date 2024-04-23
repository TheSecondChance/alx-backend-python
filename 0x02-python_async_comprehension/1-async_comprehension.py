#!/usr/bin/env python3
"""async comprehension that return list then random float"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async comprehension retun list of float"""
    return [i async for i in async_generator()]
