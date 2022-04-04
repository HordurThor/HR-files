import random
from Bucket import *


class HashMapBase:

    def __init__(self, capacity=11, prime=109345121):
        self._table = capacity * [None]
        self._n = 0
        self._prime = prime
        self._scale = 1 + random.randrange(prime-1)
        self._shift = random.randrange(prime)

    def _hash_function(self, key):
        return (hash(key)*self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n
    
    def __getitem__(self, key):
        return self.find(key)
    
    def __setitem__(self, key, value):
        self.insert(key, value)

    def __delitem__(self, key):
        self.remove(key)
    
    def items(self):
        for bucket in self._table:
            if bucket is not None:
                for item in bucket:
                    yield item

    def _rebuild(self, cap):
        old = list(self.items())
        self._table = cap * [None]
        self._n = 0
        for key, value in old:
            self[key] = value
            


class HashMap(HashMapBase):


    def insert(self, key, value):
        j = self._hash_function(key)
        if self._table[j] is None:
            self._table[j] = Bucket()
        oldsize = len(self._table[j])
        self._table[j].insert(key, value)
        if len(self._table[j]) > oldsize:
            self._n += 1
        if self._n > len(self._table) // 2:
            self._rebuild(2*len(self._table)-1)

    def update(self, key, value):
        j = self._hash_function(key)
        bucket = self._table[j]
        if bucket is None:
            raise NotFoundException()
        bucket.update(key, value)

    def find(self, key):
        j = self._hash_function(key)
        bucket = self._table[j]
        if bucket is None:
            raise NotFoundException()
        return bucket[key]

    def contains(self, key):
        j = self._hash_function(key)
        bucket = self._table[j]
        if bucket is None:
            return False
        return key in bucket

    def remove(self, key):
        j = self._hash_function(key)
        bucket = self._table[j]
        if bucket is None:
            raise NotFoundException()
        bucket.remove(key)
        self._n -= 1


