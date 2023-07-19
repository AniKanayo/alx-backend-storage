#!/usr/bin/env python3

import redis
import uuid
from typing import Union, Callable, Optional


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
        It can return the data in different formats depending on the
        function supplied
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
