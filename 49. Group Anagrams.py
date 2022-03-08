#49. Group Anagrams

class Solution(object):
	def groupAnagrams(self, strs):
		result=collections.defaultdict(list)
		for i in strs:
			result[tuple(sorted(i))].append(i)
		return result.values()
"""
Complexity Analysis: (O(NK log K), O(NK))
Time Complexity: O(NKlogK), where NN is the length of strs, and KK is the maximum length of a string in strs. The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(KlogK) time.
Space Complexity: O(NK), the total information content stored in ans.
"""

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""