class Solution:
    def majorityElement(self, nums):
        counts=collections.Counter(nums)
        return max(counts.keys(),key=counts.get)
    """
    O(n)
    O(n)
    """
    def majorityElement2(self, nums): #Time complexity : O(n**2), Space complexity : O(1)
        majority_count=len(nums)//2

        for num in nums:
            count = sum(1 for elem in nums if elem==num)
            if count > majority_count:
                return num

    def majorityElement3(self, nums): #Time complexity : O(n log n), Space complexity : O(1)
        nums.sort()
        return nums[len(n)//2]
  

    """
  Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
  """
