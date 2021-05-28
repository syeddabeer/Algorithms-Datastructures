#lru cache calls for ordered dictionary from collections.
#there are ways to do lru cache using linked list, linknode
from collections import OrderedDict

class LRUCache:
    
    def __init__(self, capacity=10):
        self.cache = OrderedDict()
        self.capacity = capacity
        
    def get(self, key):
        if key not in self.cache:
            pass
            return -1
        else:
            #value is temporary variable to store value of key
            value=self.cache[key]
            #delete the key value pair
            del self.cache[key]
            #insert key value pair so as to show the usage
            self.cache[key]=value
            #return the value
            return value

    def put(self, key, value):
        if key in self.cache: # if key is found
            # deleting the key value pair
            del self.cache[key]
            #inserting the key value pair again to show recent use
            self.cache[key]=value
        elif len(self.cache)== self.capacity: # if key is not found, and new addition is reqd. and capacity is full.
            self.cache.popitem(last=False) # least recently used item is popitem'd
            self.cache[key]=value             #new key value pair is added      
        else:
            self.cache[key]=value           #new key value pair is added  

cap=2
lRUCache = LRUCache(cap)
print("define cache of capacity:", cap)

print(lRUCache.put(1, 1)); # cache is {1=1}
print(lRUCache.cache)

lRUCache.put(2, 2); # cache is {1=1, 2=2}
print(lRUCache.cache)

lRUCache.get(1);    # return 1
print(lRUCache.cache)

lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.cache)

print(lRUCache.get(2));    # returns -1 (not found))


lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.cache)

print(lRUCache.get(1));   # return -1 (not found))

lRUCache.get(3);    # return 3
print(lRUCache.cache)

lRUCache.get(4);    # return 4
print(lRUCache.cache)