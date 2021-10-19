"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","luther"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
"""

class Solution:
    def isAlienSorted(self, words, order):
        order_map={}
        
        for index, value in enumerate(order):
            #order map is created. with letter as index and position as value.
            order_map[value] = index
            
        for i in range(0, len(words)-1, 1):
            for j in range(0, len(words[i])):
                
                # first word is similar to second word. but first word is longer. like apple, app
                if j >= len(words[i+1]):
                    return False
                
                if words[i][j] != words[i+1][j]:
                    if order_map[words[i][j]] > order_map[words[i+1][j]]:
                        return False
                    break

        return True

words1=["hello","luther"]
order1="hlabcdefgijkmnopqrstuvwxyz"
print(Solution().isAlienSorted(words1, order1))

words2=["word","world","row"]
order2="worldabcefghijkmnpqstuvxyz"
print(Solution().isAlienSorted(words2, order2))

words2=["apple","app"]
order2="abcdefghijklmnopqrstuvwxyz"
print(Solution().isAlienSorted(words2, order2))