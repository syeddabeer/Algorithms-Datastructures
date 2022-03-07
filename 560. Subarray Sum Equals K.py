#560. Subarray Sum Equals K

class Solution:
	def subarraySum(self, nums, k):
		dict={0:1} #number of occurences
		sum = 0
		count = 0
		for i in range(0, len(nums)):
			sum+=nums[i]
			if sum-k in dict:
				count+=dict[sum-k]
			if sum in dict:
				dict[sum]+=1
			else:
				dict[sum]=1
			
		return count

"""
dict={1:1, } count=1

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""