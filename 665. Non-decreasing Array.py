#665. Non-decreasing Array

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        num_violations = 0
        for i in range(1, len(nums)):
            
            if nums[i - 1] > nums[i]:
                
                if num_violations == 1:
                    return False
                
                num_violations += 1
                
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                    
        return True

"""
Complexity Analysis

Time Complexity: O(n) considering there are nn elements in the array and we process each element at most once.

Space Complexity: O(1) since we don't use any additional space apart from a couple of variables for executing this algorithm.
"""

"""
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
"""