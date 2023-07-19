#!/usr/bin/env python3

import redis
import uuid
from typing import Callable, Optional, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times a method is called."""
    key = f'{method.__qualname__}'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increment key value every time a method is called."""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of method inputs and outputs."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Creating keys for storage:
        inputs_key = f'{method.__qualname__}:inputs'
        outputs_key = f'{method.__qualname__}:outputs'

        # String to save in Redis as inputs
        str_args = ', '.join(map(str, args))

        # Use RPUSH to add inputs to Redis
        self._redis.rpush(inputs_key, str_args)

        # Compute the output of the method
        output = method(self, *args, **kwargs)

        # Use RPUSH to add output to Redis
        self._redis.rpush(outputs_key, str(output))

        return output

    return wrapper


class Cache:
    """
    Cache class for a basic caching system.
    Args:
        data: The data which will be passed as a str, bytes, int or float.
    """
    def __init__(self):
        """ Instantiate a redis object and applies a flushdb() """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a random key and
        return the key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float]:
        """
        The get method retrieves data from redis by key.
        It can return the data in different formats depending
        on the function supplied
        """
        data = self._redis.get(key)
        if fn is None or data is None:
            return data
        return fn(data)

    def get_str(self, key: str) -> Optional[str]:
        """
        The get_str method gets the redis value as a string
        """
        return self.get(key, fn=lambda data: data.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        The get_int method gets the redis value as an integer
        """
        return self.get(key, fn=int)
