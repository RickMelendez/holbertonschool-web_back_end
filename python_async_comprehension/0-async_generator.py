#!/usr/bin/env python3

"""
Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.

Yields:
i: yield a random number between 0 and 10
"""

import random
from typing import Generator
from asyncio import sleep


async def async_generator() -> Generator[float, None, None]:
    """
    Create an asynchronous generator that yields numbers from 0 to 10.
    """
    for _ in range(10):
        await sleep(1)
        yield random.uniform(0, 10)
