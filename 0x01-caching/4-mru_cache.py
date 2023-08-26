#!/usr/bin/python3

""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines a caching system with MRU algorithm
    """
    def __init__(self):
        """ Initialize MRUCache
        """
        super().__init__()
        """The list stores the keys in the order they are accessed,
        with the most recently accessed key at the front (index 0)
        """
        self.access_order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:

            # If the key is already in the cache, move it to the front
            if key in self.cache_data:
                self.access_order.remove(key)

            # Check if cache is full
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:

                # Remove the most recently used key
                mru_key = self.access_order.pop(0)

                # Remove the corresponding item from cache
                del self.cache_data[mru_key]

                print("DISCARD:", mru_key)

            # Add the new item to cache and update the access order
            self.cache_data[key] = item
            self.access_order.insert(0, key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            """ Move the accessed item to the front
            of the access order list (MRU position)
            """
            self.access_order.remove(key)
            self.access_order.insert(0, key)
            return self.cache_data[key]
        return None
