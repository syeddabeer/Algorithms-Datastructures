#1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums)==0: return 0
        if len(nums)==1: return 1
        
        left=0
        right=1
        
        maxlen=1
        
        currentMax=nums[0]
        currentMin=nums[0]
        
        while left<=right and right<len(nums):
            currentMax = max(currentMax, nums[right])
            currentMin = min(currentMin, nums[right])
            
            if currentMax - currentMin <= limit:
                maxlen = max(maxlen, right-left+1)
            else:
                if nums[left]==currentMax:
                	currentMax=max(nums[left+1:right+1])
                if nums[left]==currentMin:
                	currentMin=min(nums[left+1:right+1])
                left+=1
            right+=1
        return maxlen


"""

"""

Solution #2:
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxlengthSubarray=0
        
        if not nums:
            return 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i==j:
                    subarray=[nums[i]]
                else:
                    subarray=nums[i:j+1]
                diff = max(subarray) - min(subarray)
                if diff <= limit:
                    maxlengthSubarray= max(maxlengthSubarray, len(subarray))
        return maxlengthSubarray


"""
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
"""