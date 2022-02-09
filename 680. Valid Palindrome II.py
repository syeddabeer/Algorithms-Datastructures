class Solution:
    def validPalindrome(self, s):
        left = 0
        right = len(s)-1
        while left < right:
            if s[left]==s[right]:
                left += 1
                right -= 1
            else:
                s1=s[left:right]
                s2=s[left+1:right+1]
                return s1==s1[::-1] or s2==s2[::-1]
        return True
    
s1="abc"
sol=Solution()
print(sol.validPalindrome(s1))

s2="abca"
sol=Solution()
print(sol.validPalindrome(s2))

s2="aba"
sol=Solution()
print(sol.validPalindrome(s2))


"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
"""