# 0x01. Python - Async

## Project Overview

This project is focused on understanding and using asynchronous programming in Python using the `asyncio` library. It involves writing coroutines, running concurrent coroutines, and measuring the runtime of asynchronous tasks. By the end of this project, you will be able to use the `async` and `await` syntax, work with asynchronous I/O, and understand how to manage concurrency in Python programs.

### Project Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python3 (version 3.7).
- All your files should end with a new line.
- All your files must be executable.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- Your code should adhere to the `pycodestyle` style (version 2.5.x).
- All your functions and coroutines must be type-annotated.
- All your modules and functions must have documentation.

## Learning Objectives

By the end of this project, you are expected to be able to explain the following:

- `async` and `await` syntax
- How to execute an async program with `asyncio`
- How to run concurrent coroutines
- How to create asyncio tasks
- How to use the `random` module in asynchronous tasks

## Project Tasks

### 0. The Basics of Async

Write an asynchronous coroutine `wait_random` that takes an integer argument (`max_delay`) with a default value of 10. The function should wait for a random delay between 0 and `max_delay` seconds and eventually return the delay.

Example:
```python
#!/usr/bin/env python3
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
