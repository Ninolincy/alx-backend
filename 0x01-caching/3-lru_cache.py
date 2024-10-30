#!/usr/bin/env python3

""" LRU Caching """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching algorithm """
    def __init__(self):
        """ Initialize cache"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    least_key = self.cache_data.popitem()
                    """discard least recently used item"""
                    print("DISCARD: {}".format, least_key)
            self.cache_data[key] = item

    def get(self, key):
        """ return the value of key in cache """
        return self.cache_data.get(key)
