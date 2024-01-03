#!/usr/bin/env python3
"""module creates a class BasicCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesn't have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn't exist in self.cache_data, return None.
"""
BaseCaching = __import__('0-base_caching').BaseCaching


class BasicCache(BasicCache):
    """a caching system"""
    def put(self, key, item):
        """sets key in cache"""
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item   

    def get(self, key):
        """gets value of cache with key"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
