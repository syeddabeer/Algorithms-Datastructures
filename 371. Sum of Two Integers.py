"""
371. Sum of Two Integers
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1: 
Input: a = 1, b = 2
Output: 3
Example 2:
Input: a = 2, b = 3
Output: 5
Constraints:
-1000 <= a, b <= 1000

"""

class Solution:
	def getSum(self, a, b):
		mask = 0xffffffff
		while (b & mask) > 0:
			carry = (a & b) << 1
			a = a ^ b 
			b = carry 

		return (a & mask) if b > 0 else a

myobj = Solution()
a = 2
b = 3
print(myobj.getSum(a,b)) 