class Solution:
    def isIsomorphic(self, s, t):
        dict_s_to_t = {}
        dict_t_to_s = {}
        
        for i, j in zip(s, t):
            if i not in dict_s_to_t and j not in dict_t_to_s:
                dict_s_to_t[i]=j
                dict_t_to_s[j]=i
            
            # elif dict_s_to_t[i]!=j or dict_t_to_s[j]!=i:
            elif dict_s_to_t.get(i) != j or dict_t_to_s.get(j) != i:
                return False
        
        return True
          
"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""