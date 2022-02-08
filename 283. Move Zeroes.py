class Solution:
    def moveZeroes(self, nums):
        zero = 0
        for i in range(len(nums)):
            #print("nums: ".format(nums))
            if nums[i] != 0:
                # first time: zeroth index element swapped with itself
                nums[i], nums[zero] = nums[zero], nums[i]
                print("nums: ".format(nums))
                zero+=1
        return nums

"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"