class Solution:
    def maxSubArray(self, num):
        currentSubArray = num[0]
        maximumvalue = num[0]
        
        for i in range(1, len(num)):
            currentSubArray = max(num[i], currentSubArray+num[i])
            maximumvalue = max(maximumvalue, currentSubArray)
        
        return maximumvalue

    def maxSubArray2(self, num):
        currentSum = 0
        maximumvalue = float('-inf')
        
        for num in num[0:]:
            currentSum += num

            if currentSum > maximumvalue:
                maximumvalue = currentSum

            if currentSum<0:
                currentSum=0 
        
        return maximumvalue

myobj=Solution()
nums1=[-2,1,-3,4,-1,2,1,-5,4]
nums2=[5,4,-1,7,8]
print(myobj.maxSubArray2(nums1))
print(myobj.maxSubArray2(nums2))

"""
time: O(N)
space: O(1)

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
"""