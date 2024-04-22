# Python Asyncio  

Asyncio is a Python library that is used for concurrent programming, including the use of async iterator in Python.   

It is not multi-threading or multi-processing.  

Asyncio is used as a foundation for multiple python asynchronous frameworks that provide high-performance network and web servers, database connection libraries, distributed task queues, etc


## How Asyncio Works

At the core of Asyncio is the event loop, which acts as a traffic cop for managing asynchronous tasks. Here’s a simplified overview of how Asyncio works:

1. [[Coroutines]]: You define asynchronous functions using the `async def` syntax, creating coroutines. These functions can be paused and resumed, allowing other tasks to run while waiting for I/O operations.
2. Event Loop: You create an event loop, which is responsible for managing the execution of coroutines. It schedules tasks, tracks their progress, and ensures that I/O operations do not block the entire program.
3. `await` Keyword: Within a coroutine, you use the `await` keyword to delegate control back to the event loop when waiting for asynchronous operations to complete. This ensures that other tasks can continue running in the meantime.
4. Concurrent Execution: The event loop juggles multiple tasks concurrently, efficiently using system resources. When a task awaits an I/O operation, the event loop switches to another task, keeping the program responsive.


## Example:

```
  import asyncio


  async def func1():
  	print("Function 1 started..")
  	await asyncio.sleep(2)
  	print("Function 1 Ended")
  
  
  async def func2():
  	print("Function 2 started..")
  	await asyncio.sleep(3)
  	print("Function 2 Ended")
  
  
  async def func3():
  	print("Function 3 started..")
  	await asyncio.sleep(1)
  	print("Function 3 Ended")
  
  
  async def main():
  	L = await asyncio.gather(
  		func1(),
  		func2(),
  		func3(),
  	)
  	print("Main Ended..")
  
  
  asyncio.run(main())
```
