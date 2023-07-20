#!/usr/bin/env python3
"""
This module extends the caching capabilities of our previous design by
keeping a history of all inputs and their corresponding outputs.
"""

import redis
import uuid
from typing import Callable, Optional, Union, Any
from functools import wraps


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a
    particular function.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args: Any, **kwargs: Any) -> Any:
        """
        Store the input and output data to redis
        """
        method_name = method.__qualname__
        inputs = str(args)
        self._redis.rpush(f"{method_name}:inputs", inputs)
        result = method(self, *args, **kwargs)
        self._redis.rpush(f"{method_name}:outputs", str(result))
        return result
    return wrapper


class Cache:
    """
    Cache class for a caching system with input/output history
    """

    def __init__(self):
        """ Initialize a redis object and applies a flushdb() """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a random key and return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float]:
        """
        The get method retrieves data from redis by key
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
