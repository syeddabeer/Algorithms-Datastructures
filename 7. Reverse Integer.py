class Solution:
    def reverse(self, x: int) -> int:
        min=-2**31
        max=2**31 - 1
        if x not in range(min, max): # handle buffer overflow
            return 0 
        elif x>=0:
            a = int(str(x)[::-1])
            if a not in range(min, max):
                return 0
            else:
                return a
        else:
            a = int(str(x*-1)[::-1])
            a = a*-1
            if a not in range(min, max):
                return 0
            else:
                return a
"""
time complexity for above is O(log(n))

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321
Example 2:
Input: x = -123
Output: -321
Example 3:
Input: x = 120
Output: 21
Constraints:
-231 <= x <= 231 - 1
"""
