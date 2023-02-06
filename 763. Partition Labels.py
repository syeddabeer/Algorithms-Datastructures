#763. Partition Labels

"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.


class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        print(f"last is {last}")
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            print(f"i is {i}")
            print(f"c is {c}")
            j = max(j, last[c])
            print(f"j is {j}")
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
                print(f"ans is {ans}")
            
        return ans

last is {'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11, 'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21}
i is 0
c is a
j is 8
i is 1
c is b
j is 8
i is 2
c is a
j is 8
i is 3
c is b
j is 8
i is 4
c is c
j is 8
i is 5
c is b
j is 8
i is 6
c is a
j is 8
i is 7
c is c
j is 8
i is 8
c is a
j is 8
ans is [9]
i is 9
c is d
j is 14
i is 10
c is e
j is 15
i is 11
c is f
j is 15
i is 12
c is e
j is 15
i is 13
c is g
j is 15
i is 14
c is d
j is 15
i is 15
c is e
j is 15
ans is [9, 7]
i is 16
c is h
j is 19
i is 17
c is i
j is 22
i is 18
c is j
j is 23
i is 19
c is h
j is 23
i is 20
c is k
j is 23
i is 21
c is l
j is 23
i is 22
c is i
j is 23
i is 23
c is j
j is 23
ans is [9, 7, 8]

"""