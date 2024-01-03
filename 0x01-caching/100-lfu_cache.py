
"""module creates a class LFUCache that inherits from
BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don't
forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the least frequency used item (LFU algorithm)
if you find more than 1 item to discard, you must use the LRU algorithm
to discard only the least recently used
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn't exist in self.cache_data, return None."""

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """a caching system - LRU"""
    def __init__(self):
        """inits cache"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def put(self, key, item):
        """sets item in cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD: {}".format(lfu_key))
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            for i, key_freq in enumerate(self.keys_freq):
                if key_freq[1] == 0:
                    ins_index = i
                    break
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            max_positions = []
            mru_freq = 0
            mru_pos = 0
            ins_pos = 0
            for i, key_freq in enumerate(self.keys_freq):
                if key_freq[0] == key:
                    mru_freq = key_freq[1] + 1
                    mru_pos = i
                    break
                elif len(max_positions) == 0:
                    max_positions.append(i)
                elif key_freq[1] < self.keys_freq[max_positions[-1]][1]:
                    max_positions.append(i)
            max_positions.reverse()
            for pos in max_positions:
                if self.keys_freq[pos][1] > mru_freq:
                    break
                ins_pos = pos
            self.keys_freq.pop(mru_pos)
            self.keys_freq.insert(ins_pos, [key, mru_freq])

    def get(self, key):
        """gets item by key"""
        if key is not None and key in self.cache_data:
            max_positions = []
            mru_freq = 0
            mru_pos = 0
            ins_pos = 0
            for i, key_freq in enumerate(self.keys_freq):
                if key_freq[0] == key:
                    mru_freq = key_freq[1] + 1
                    mru_pos = i
                    break
                elif len(max_positions) == 0:
                    max_positions.append(i)
                elif key_freq[1] < self.keys_freq[max_positions[-1]][1]:
                    max_positions.append(i)
            max_positions.reverse()
            for pos in max_positions:
                if self.keys_freq[pos][1] > mru_freq:
                    break
                ins_pos = pos
            self.keys_freq.pop(mru_pos)
            self.keys_freq.insert(ins_pos, [key, mru_freq])
        return self.cache_data.get(key, None)
