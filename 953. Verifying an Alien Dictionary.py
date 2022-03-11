class Solution:
    def isAlienSorted(self, words, order):
        order_map ={}
        for index, val in enumerate(order):
            order_map[val]=index 
        
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                # border condition - first word is larger
                if j >= len(words[i+1]): return False
            
                if words[i][j] != words[i+1][j]:
                    if order_map[words[i][j]] > order_map[words[i+1][j]]:
                        return False
                    break
        return True
"""
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
"""