"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
class Solution:
    def containsDuplicate(self, nums):
        """
        Approach: One-Liner with HashSet
        """
        return len(set(nums)) != len(nums)

        # O(n) time.
        # O(n) auxiliary space.
        # O(n) total space.


    def containsDuplicate2(self, nums):
        """
        Approach: HashSet
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False

myobj=Solution()
nums1=[1,2,3,1]
nums2=[1,2,3,4]
nums3=[1,1,1,3,3,4,3,2,4,2]
print(myobj.containsDuplicate(nums1))
print(myobj.containsDuplicate(nums2))
print(myobj.containsDuplicate(nums3))

"""
Approach 1: One-Liner with HashSet

Time complexity:

O(n), where n is the number of elements in the list.
Explanation: Converting a list to a set and comparing lengths both require linear time.
Space complexity:

O(n)
Explanation: The set used to store unique elements can contain up to n elements in the worst case.
"""

"""
Approach 2: Iterative Approach using HashSet
Time complexity:

O(n), where n is the number of elements in the list.
Explanation: We iterate through the list once, performing O(1) operations for each element.
Space complexity:

O(n)
Explanation: The set used to store seen elements can contain up to n elements in the worst case.
"""