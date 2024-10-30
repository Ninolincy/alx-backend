#!/usr/bin/env python3

""" LFU Caching """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU caching algorithm """
    def __init__(self):
        """ Initialize cache"""
        super().__init__()
        self.cache_usage = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    least_key = min(self.cache_usage, key=self.cache_usage.get)
                    del self.cache_data[least_key]
                    del self.cache_usage[least_key]
                    """discard least frequently used item"""
                    print("DISCARD: {}".format(least_key))
            self.cache_data[key] = item
            self.cache_usage[key] = 0
        else:
            pass

    def get(self, key):
        """ return the value of key in cache """
        if key in self.cache_data:
            self.cache_usage[key] += 1
            return self.cache_data[key]
        return None
