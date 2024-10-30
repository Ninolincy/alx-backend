#!/usr/bin/env python3
""" FIFO cache """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache class
    """
    def __init__(self) -> None:
        """ Constructor method to initialize FIFO"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                """discard old items(FIFO algorithm)"""
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))

    def get(self, key):
        """ return the value of key in cache """
        return self.cache_data.get(key)
