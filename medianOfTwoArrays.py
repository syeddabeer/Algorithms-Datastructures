"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for j in range(0, len(nums2), 1):
            nums1.append(nums2[j])
        nums1.sort()
        return self.findmedian(nums1)

    def findmedian(self, nums):
        if len(nums) == 0:
            return 
        elif len(nums)%2 == 0:
            middleindex=(len(nums)//2)-1
            middlemostnumber = (nums[middleindex] + nums[middleindex+1])/2.0
            return middlemostnumber
        else:
            middlemostnumber = nums[(len(nums)+1)//2 - 1]
            return middlemostnumber
nums1=[1,3]
nums2=[2]
a=Solution().findMedianSortedArrays(nums1, nums2)
print(a)