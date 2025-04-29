Tasks

0. Async Generator
Write a coroutine async_generator() that loops 10 times, waits 1 second asynchronously each time, and yields a random number between 0 and 10.

1. Async Comprehensions
Import async_generator and write a coroutine async_comprehension() that collects 10 random numbers using async comprehension and returns them.

2. Run time for four parallel comprehensions
Import async_comprehension and write a coroutine measure_runtime() that runs it 4 times in parallel using asyncio.gather, measures the total runtime, and returns it.
