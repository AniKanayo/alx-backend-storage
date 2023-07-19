import requests
import time
from cachetools import TTLCache
from typing import Dict

# Create a cache with an expiration time of 10 seconds
cache = TTLCache(maxsize=100, ttl=10)


def get_page(url: str) -> str:
    """
    Fetches the HTML content of a given URL using requests
    module and caches the result.

    Parameters:
        url (str): The URL to fetch the HTML content from.

    Returns:
        str: The HTML content of the URL.
    """
    if url in cache:
        return cache[url]

    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        cache[url] = html_content
        return html_content
    else:
        raise requests.HTTPError(f"Failed to fetch URL: {url}")


def cached_page_count() -> Dict[str, int]:
    """
    Returns a dictionary containing the count of cached pages for each URL.

    Returns:
        Dict[str, int]: A dictionary containing the count of cached
        pages for each URL.
    """
    return {key: cache.stats(key).current for key in cache.keys()}


# Decorator for caching the result of the get_page function
def cached_get_page(func):
    def wrapper(url):
        if url in cache:
            return cache[url]

        html_content = func(url)
        cache[url] = html_content
        return html_content

    return wrapper


@cached_get_page
def slow_get_page(url: str) -> str:
    """
    Fetches the HTML content of a given URL using requests module
    and caches the result with the decorator.

    Parameters:
        url (str): The URL to fetch the HTML content from.

    Returns:
        str: The HTML content of the URL.
    """
    time.sleep(2)  # Simulate a slow response
    return get_page(url)
