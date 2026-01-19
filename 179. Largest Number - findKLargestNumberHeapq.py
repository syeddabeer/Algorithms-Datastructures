class Solution1:
    def largestKnumber(self, nums, k):
        nums.sort()
        return nums[-k]
import heapq
class Solution2: #heap method.
    def largestKnumber(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
    
sol1=Solution1()
sol2=Solution2()
nums = [3,2,1,5,6,4]
k = 2
print(sol1.largestKnumber(nums, k))
print(sol2.largestKnumber(nums, k))

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert each integer to a string
        num_strings = [str(num) for num in nums]

        # Sort strings based on concatenated values
        num_strings.sort(key=lambda a: a * 10, reverse=True)

        # Handle the case where the largest number is zero
        if num_strings[0] == "0":
            return "0"

        # Concatenate sorted strings to form the largest number
        return "".join(num_strings)

Time Complexity: O(nlogn)
Space Complexity: O(n+S)

"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.
Example 1:
Input: nums = [10,2]
Output: "210"
Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
"""