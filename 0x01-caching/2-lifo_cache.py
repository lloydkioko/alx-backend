#!/usr/bin/env python3
"""
LIFOCache class implementation
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Defines a caching system class that implements LIFO algorithm
    """
    def __init__(self):
        """
        Initializes the class
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data the item value for the key,
        checking that BaseCaching.MAX_ITEMS isn't exceeded. Else, discard first
        item following LIFO algorithm
        """
        if key and item:
            self.cache_data.update({key: item})

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.last_inserted)
                print("DISCARD: {}".format(self.last_inserted))

            self.last_inserted = key

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key
        """
        return self.cache_data.get(key)
