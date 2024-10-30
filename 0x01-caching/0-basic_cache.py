#!/usr/bin/env python3
""" Basic dictionary"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    
    def put(self, key, item):
        """ assign to dictionary item the value of key"""
        if key and item:
            self.cache_data[key] = item
    
    def get(self, key):
        """ return the value of key in cache """
        return self.cache_data.get(key)