<<<<<<< HEAD
class Solution:
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda x:x[1]-x[0])
        energy=0
        for task in tasks:
            energy = task[0]+max(energy, task[1]-task[0])
        return energy
=======
#17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits):
        my_dict={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        for digit in digits: #digits is a string
            results=[]
            if len(results)==0:
                results = [iter for iter in my_dict[digit]]
            else:
                results = [prev+new for prev in results for new in my_dict[digit]]
        return results  


"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""
>>>>>>> 92e67955568d26cebd4e7199b0ec0b1911f37865
