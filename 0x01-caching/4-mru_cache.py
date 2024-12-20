#!/usr/bin/env python3

""" MRU Caching """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU caching algorithm """
    def __init__(self):
        """ Initialize cache"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    most_key = self.cache_data.popitem()
                    """discard most recently used item"""
                    print("DISCARD: {}".format, most_key)
            self.cache_data[key] = item

    def get(self, key):
        """ return the value of key in cache """
        return self.cache_data.get(key)
