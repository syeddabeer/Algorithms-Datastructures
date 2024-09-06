class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        elif x==int(str(x)[::-1]):
            return True
        else:
            return False
          
class Solution(object):
    def isPalindromeFollowUp(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        
        reversed = 0
        temp = x

        while temp!=0:
            digit = temp % 10
            reversed = reversed*10 + digit
            temp //= 10
        
        return reversed==x

"""
for follow up method:
Time Complexity: (O(\log_{10} x))
Space Complexity: (O(1))
****
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""
