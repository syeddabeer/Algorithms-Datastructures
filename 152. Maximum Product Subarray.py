"""
152. Maximum Product Subarray

Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    def maxProductSubArray(self, nums):
    	currMinProduct , currMaxProduct = nums[0], nums[0]
    	result = nums[0]
    	for i in range(1, len(nums), 1):
    		# compulsory to use a, b format. because we want to update curr max product, curr min product at the same time using values from previous iteration.
    		currMaxProduct, currMinProduct = max(nums[i], nums[i]*currMaxProduct, nums[i]*currMinProduct), min(nums[i], nums[i]*currMaxProduct, nums[i]*currMinProduct) 	
    		result = max(result, currMaxProduct)
    		
    	return result
    	
myobj=Solution()
nums1=[2,3,-2,4]
nums2 = [-2,0,-1]
nums3=[-2,3,-2,4,-4]
print(myobj.maxProductSubArray(nums1))
print(myobj.maxProductSubArray(nums2))
print(myobj.maxProductSubArray(nums3))

#time complexity - O(n)
#space complexity - O(1)