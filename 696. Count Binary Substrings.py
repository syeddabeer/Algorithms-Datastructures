class Solution(object):
    def countBinarySubstrings(self, s):
        ans, prev, cur = 0, 0, 1
        for i in xrange(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        return ans + min(prev, cur)

#time complexity: O(N), where N is the length of s. Every loop is through O(N) items with O(1) work inside the for-block.
#space complexity: O(1), the space used by prev, cur, and ans.
"""
696. Count Binary Substrings
Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.
Example 1:
Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

This solution counts substrings of a binary string where all 0’s and all 1’s are grouped together and the counts of 0’s and 1’s are equal. It works by processing the string in a single pass, grouping consecutive same characters into runs. The variables prev and cur track the lengths of the previous and current runs of 0’s or 1’s. Whenever the character changes (i.e., at a 0→1 or 1→0 boundary), the code adds min(prev, cur) to the answer, because that’s the maximum number of valid substrings that can cross this boundary. Inside the same run, cur is simply incremented to extend the current group. The last boundary is handled after the loop by adding min(prev, cur) one final time. This ensures all valid cross‑boundary substrings are counted exactly once per occurrence, matching the problem’s requirement.


"""