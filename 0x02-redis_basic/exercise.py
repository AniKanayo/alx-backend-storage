#!/usr/bin/env python3

import redis
import uuid
from typing import Callable, Optional, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """decorator to count the number of times a method is called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increment key value every time a method is called"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """decorator to store the history of inputs and outputs
    for a particular function"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Append the input arguments and the output to lists in Redis"""
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(inputs_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))
        return result

    return wrapper


class Cache:
    """
    Cache class for a basic caching system
    Args:
        data: the data which will be passed as a str, bytes, int or float.
    """
    def __init__(self):
        """ Instantiate a redis object and applies a flushdb() """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a random key and return the key.
        This method is decorated with 'count_calls' to count the number
        of times it is called,
        and 'call_history' to keep a history of its inputs and outputs.
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

    def replay(self, fn: Callable):
        """
        Display the history of calls of a particular function.
        """
        inputs_key = f"{fn.__qualname__}:inputs"
        outputs_key = f"{fn.__qualname__}:outputs"
        inputs_list = self._redis.lrange(inputs_key, 0, -1)
        outputs_list = self._redis.lrange(outputs_key, 0, -1)
        print(f"{fn.__qualname__} was called {len(inputs_list)} times:")
        for inp, out in zip(inputs_list, outputs_list):
            print(f"{fn.__qualname__}(*{inp.decode('utf-8')}) -> \"
                  "{out.decode('utf-8')}")
