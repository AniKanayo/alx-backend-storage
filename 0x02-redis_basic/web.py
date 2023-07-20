#!/usr/bin/env python3
"""
Module Documentation
A module that handles web page caching and access counting.
"""

import requests
import redis
from typing import Callable
from functools import wraps

r = redis.Redis()


def count_url_calls(func: Callable) -> Callable:
    """
    Decorator for counting how many times a URL has been accessed.
    """
    @wraps(func)
    def wrapper(url: str) -> str:
        key = f'count:{url}'
        r.incr(key)
        return func(url)

    return wrapper


def cache_response(func: Callable) -> Callable:
    """
    Decorator for caching a function's response.
    """
    @wraps(func)
    def wrapper(url: str) -> str:
        key = f'cache:{url}'
        cached_response = r.get(key)
        if cached_response is not None:
            return cached_response
        response = func(url)
        r.setex(key, 10, response)
        return response

    return wrapper


@count_url_calls
@cache_response
def get_page(url: str) -> str:
    """
    Function for retrieving the HTML content of a web page.
    """
    response = requests.get(url)
    return response.text
