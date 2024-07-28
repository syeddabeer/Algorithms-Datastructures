"""
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
class Solution:
	def ProductExceptSelf(self, nums):
		n=len(nums)
		prefix_product = 1 
		postfix_product = 1 
		result = [0]*n 

		for i in range(0, n, 1):
			result[i] = prefix_product
			prefix_product *= nums[i]

		for j in range(n-1, -1, -1):
			result[j] *= postfix_product
			postfix_product *= nums[j]

		return result 

myobj = Solution()
nums1 = [1,2,3,4]
nums2 = [-1,1,0,-3,3]
print(myobj.ProductExceptSelf(nums1))
print(myobj.ProductExceptSelf(nums2))
