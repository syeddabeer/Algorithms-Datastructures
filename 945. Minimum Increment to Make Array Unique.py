#945. Minimum Increment to Make Array Unique

#II Solution:
class Solution:
    def minIncrementForUnique(self, nums):
        max_val = max(nums)
        count = collections.Counter(nums)
        print(count)
        taken = []
        
        moves = 0
        for x in range(len(nums) + max_val):
            if count[x] >= 2:
                taken.extend([x] * (count[x] - 1))
            elif taken and count[x] == 0:
                moves += x - taken.pop()
                
        return moves



"""
Let NN be the length of nums and MM be the maximum value in nums.

Time Complexity: O(N + M)O(N+M)

We iterate over every possible value of x from 1 to N + MN+M and each iteration requires O(1)O(1) time.
Space Complexity: O(N + M)O(N+M)

In the Java implementation, O(N + M)O(N+M) space is allocated for count and O(1)O(1) space for taken. In the Python implementation, a hash map is used for count which will contain at most NN elements when every value in the input array is unique. A list is used for taken which will contain N - 1N−1 elements when every value in the input array is the same. Thus the Java implementation uses O(N + M)O(N+M) space while the python implementation uses O(N)O(N) space.
"""






class Solution:
    def minIncrementForUnique(self, arr: List[int]) -> int:
        if not arr:
            return 0
        arr.sort()
        s, count = arr[0], 0
        for i in arr:
            count += max(0, s - i)
            s = max(s + 1, i + 1)
        return count
"""
Complexity Analysis

Let NN be the length of nums.

Time Complexity: O(NlogN)+O(N) = O(NlogN)

Sorting the array requires O(NlogN) time and iterating over each element in the array requires O(N) time.
Space Complexity: O(N)

Additional space is required while sorting the array in place. How much additional space depends on the specific implementation of the built in sort.
"""

"""
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
Return the minimum number of moves to make every value in nums unique.

Example 1:
Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].

Example 2:
Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
"""


