# Asynchronous Comprehensions in Python 

 You can traverse an asynchronous generator or asynchronous iterator using an asynchronous comprehension via the “async for” expression.

## What are Asynchronous Comprehensions
An async comprehension is an asynchronous version of a classical comprehension.  

Asyncio supports two types of asynchronous comprehensions, they are the “async for” comprehension and the “await” comprehension.

## Comprehensions
Comprehensions allow data collections like lists, dicts, and sets to be created in a concise way.

List comprehensions provide a concise way to create lists.

— LIST COMPREHENSIONS
A list comprehension allows a list to be created from a for expression within the new list expression.  


```
  # create a list using a list comprehension  
  result = [a*2 for a in range(100)]
```
 
Comprehensions are also supported for creating dicts and sets.

For example:
```
  # create a dict using a comprehension
  result = {a:i for a,i in zip(['a','b','c'],range(3))}
  # create a set using a comprehension
  result = {a for a in [1, 2, 3, 2, 3, 1, 5, 4]}
```

## Asynchronous Comprehensions
An asynchronous comprehension allows a list, set, or dict to be created using the “async for” expression with an asynchronous iterable.

```
  # async list comprehension with an async iterator
  result = [a async for a in aiterable]
```

This will create and schedule coroutines or tasks as needed and yield their results into a list.

Recall that the “async for” expression may only be used within coroutines and tasks.

The “async for” expression allows the caller to traverse an asynchronous iterator of awaitables and retrieve the result from each.

Internally, the async for loop will automatically resolve or await each awaitable, scheduling coroutines as needed.

An async `generator` automatically implements the methods for the async iterator and may also be used in an asynchronous comprehension.

`asynchronous generator`: A function which returns an asynchronous generator iterator.


## Await Comprehensions
The “await” expression may also be used within a list, set, or dict comprehension, referred to as an await comprehension.
