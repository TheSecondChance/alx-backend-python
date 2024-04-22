#!/usr/bin/env python3
'''Task 0 module.
'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for random number of seconds'''
    timeTowait = random.random() * max_delay
    await asyncio.sleep(timeTowait)
    return timeTowait
