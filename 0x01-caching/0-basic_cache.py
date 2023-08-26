#!/usr/bin/python3

"""
file conains a  class BasicCache that inherits from BaseCaching
and is a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    caching system that doesnt have a limit
    """

    def put(self, key, item):
        """add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """returns value linked to key
        """
        if key is not None:
            return self.cache_data.get(key)
