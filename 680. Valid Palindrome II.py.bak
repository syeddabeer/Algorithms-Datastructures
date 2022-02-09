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