#!/usr/bin/env python3
"""A module that contains functionality for webpage fetching and caching"""

import requests
from Cache import Cache  # import the Cache class


def cache_request(fn):
    """ A decorator for caching the result of a function call
    Args:
    fn: The function to be decorated
    """
    def wrapper(url):
        cache = Cache()
        result = cache.get(url)
        key = "count:{}".format(url)
        if result is not None:
            cache._redis.incr(key)
            return result
        else:
            result = fn(url)
            cache._redis.set(url, result, ex=10)
            cache._redis.set(key, 1, ex=10)
            return result
    return wrapper


@cache_request
def get_page(url: str) -> str:
    """Fetches the webpage content of the specified URL
    Args:
        url: The URL of the webpage
    Returns:
        The HTML content of the webpage as a string
  """
    response = requests.get(url)
    return response.text
