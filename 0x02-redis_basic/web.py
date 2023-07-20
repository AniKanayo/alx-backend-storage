#!/usr/bin/env python3

import requests
import time
from cachetools import TTLCache, cached
from typing import Dict

# Create a cache with an expiration time of 10 seconds
cache = TTLCache(maxsize=100, ttl=10)


@cached(cache)
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a given URL using requests module and
    caches the result.

    Parameters:
        url (str): The URL to fetch the HTML content from.

    Returns:
        str: The HTML content of the URL.
    """
    count_key = f"count:{url}"

    if count_key in cache:
        cache[count_key] += 1
    else:
        cache[count_key] = 1

    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        return html_content
    else:
        raise requests.HTTPError(f"Failed to fetch URL: {url}")


def cached_page_count() -> Dict[str, int]:
    """
    Returns a dictionary containing the count of cached pages for each URL.

    Returns:
        Dict[str, int]: A dictionary containing the count of cached pages
        for each URL.
    """
    return {key: cache.stats(key).current for key in cache.keys()}


if __name__ == "__main__":
    # Test the get_page function with a slow URL
    slow_url = "http://slowwly.robertomurray.co.uk/delay/5000"
    "/url/https://example.com"
    start_time = time.time()
    content = get_page(slow_url)
    end_time = time.time()
    print(f"Time taken to fetch the content:"
          "{end_time - start_time:.2f} seconds")

    # Test the cached_page_count function to get the count of cached pages
    print("Cached page count:")
    print(cached_page_count())
