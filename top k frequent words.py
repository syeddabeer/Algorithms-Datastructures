class Solution:
	def topKFrequent(self, words, k):
		d = {} # dictionary: key value pair. word can be key, and freq can be value
		for word in words:
			if word in d.keys():
				d[word] = d[word]+1
			else:
				d[word] = 1
			#d.get(word, 0) + 1

		ret = sorted(d, key=lambda word: (-d[word], word)) #compare negative values for desc
		return ret[0:k]

# - this is O(n + mlgm) time, where m is the number of unique strings in words. So O(mlgm) if m = O(n)
"""
Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
Example 1:
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
"""