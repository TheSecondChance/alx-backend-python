#!/usr/bin/env python3
"""new function task_wait_n The code is nearly identical to wait_n except
task_wait_random is being called.
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait_random n times"""
    tasks = []
    delays = []

    for i in range(n):
        waitTask = task_wait_random(max_delay)
        tasks.append(waitTask)

    for waitTask in asyncio.as_completed((tasks)):
        delay = await waitTask
        delays.append(delay)

    return delays
