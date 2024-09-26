"""
2340. Minimum Adjacent Swaps to Make a Valid Array
You are given a 0-indexed integer array nums.

Swaps of adjacent elements are able to be performed on nums.

A valid array meets the following conditions:

The largest element (any of the largest elements if there are multiple) is at the rightmost position in the array.
The smallest element (any of the smallest elements if there are multiple) is at the leftmost position in the array.
Return the minimum swaps required to make nums a valid array.
"""

class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        minval = min(nums)
        minidx = nums.index(minval)

        modified_nums = [nums[minidx]] + nums[:minidx] + nums[minidx+1:]

        maxval = max(nums)
        maxidx_fromright = modified_nums[::-1].index(maxval)

        return minidx+maxidx_fromright