# hashmap design
# hashmap is a java name, in python; it is called dict.
class Bucket:
	def __init__(self):
		self.bucket=[]

	def get(self, key):
		for (k, v) in self.bucket:
			if k == key:
				return v
		return -1

	def update(self, key, value):
		found=False
		for (i, kv) in enumerate(self.bucket):
			if key == kv[0]:
				self.bucket[i] = (key, value)
				found=True
				break
		if not found:
			self.bucket.append((key, value))

	def remove(self, key):
		for i, kv in enumerate(self.bucket):
			if key == kv[0]:
				del self.bucket[i]


class MyHashMap:
	def __init__(self):
		self.key_space=2069
		self.hash_table = [Bucket() for i in range(self.key_space)]


	def put(self, key, value):
		hash_key = key%self.key_space
		self.hash_table[hash_key].update(key, value)


	def get(self, key):
		hash_key = key%self.key_space
		return self.hash_table[hash_key].get(key)



	def remove(self, key):
		hash_key=key%self.key_space
		self.hash_table[hash_key].remove(key)


# Complexity Analysis

# Time Complexity: for each of the methods, the time complexity is \mathcal{O}(\frac{N}{K})O( 
# K
# N
# ​
#  ) where NN is the number of all possible keys and KK is the number of predefined buckets in the hashmap, which is 2069 in our case.

# In the ideal case, the keys are evenly distributed in all buckets. As a result, on average, we could consider the size of the bucket is \frac{N}{K} 
# K
# N
# ​
#  .

# Since in the worst case we need to iterate through a bucket to find the desire value, the time complexity of each method is \mathcal{O}(\frac{N}{K})O( 
# K
# N
# ​
#  ).

# Space Complexity: \mathcal{O}(K+M)O(K+M) where KK is the number of predefined buckets in the hashmap and MM is the number of unique keys that have been inserted into the hashmap.
