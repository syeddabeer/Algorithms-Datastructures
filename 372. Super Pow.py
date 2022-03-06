#372. Super Pow
class Solution:
	def superPow(self, a, b):
		c = ""
		for i in b:
			c += str(i)

		result = pow(a, int(c), 1337)
		return result

"""
Your task is to calculate a^b mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

 

Example 1:

Input: a = 2, b = [3]
Output: 8
Example 2:

Input: a = 2, b = [1,0]
Output: 1024
Example 3:

Input: a = 1, b = [4,3,3,8,5,2]
Output: 1
"""