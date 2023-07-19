#!/usr/bin/env python3
""" This is a module to demonstrate a caching system using redis """

import redis
import uuid
from typing import Union


class Cache:
    """ Cache class for a basic caching system
        Args:
        data: the data which will be passed as a str, bytes, int or float.
    """
    def __init__(self):
        """ Instantiate a redis object and applies a flushdb()
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store the input data in Redis using a random key and return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
