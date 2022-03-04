# 213. House Robber II
class Solution:
	def rob(self, nums):
		if not nums:
			return 0
		if len(nums)<=3:
			return max(nums)

		def helper(dp):
			dp[1]=max(dp[0], dp[1])

			for x in range(2, len(dp)):
				dp[x] = max(dp[x-1], dp[x]+dp[x-2])

			return dp[-1]

		p1= helper(nums[:len(nums)-1])
		p2= helper(nums[1:len(nums)])
		return max(p1, p2)

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
"""