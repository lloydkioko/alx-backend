#!/usr/bin/env python3
"""
LRUCache class implementation
"""
from base_caching import BaseCaching
from collections import deque


class LRUCache(BaseCaching):
    """
    Defines a caching system class that implements LRU algorithm
    """
    # Queue of items accessed in dictionary using get
    KEYS_ACCESSED = deque([])

    def __init__(self):
        """
        Initializes the class
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data the item value for the key,
        checking that BaseCaching.MAX_ITEMS isn't exceeded. Else, discard first
        item following LRU algorithm
        """
        if key and item:
            self.cache_data.update({key: item})

            if key in LRUCache.KEYS_ACCESSED:
                LRUCache.KEYS_ACCESSED.remove(key)
                LRUCache.KEYS_ACCESSED.append(key)
            else:
                LRUCache.KEYS_ACCESSED.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                least_used_key = LRUCache.KEYS_ACCESSED.popleft()
                self.cache_data.pop(least_used_key)
                print("DISCARD: {}".format(least_used_key))

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key
        """
        if key in LRUCache.KEYS_ACCESSED:
            LRUCache.KEYS_ACCESSED.remove(key)
            LRUCache.KEYS_ACCESSED.append(key)

        return self.cache_data.get(key)
