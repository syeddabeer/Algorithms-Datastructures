"""
2272. Substring With Largest Variance
The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "aababbb"
Output: 3
Explanation:
All possible variances along with their respective substrings are listed below:
- Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
- Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
- Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
- Variance 3 for substring "babbb".
Since the largest possible variance is 3, we return it.
Example 2:

Input: s = "abcde"
Output: 0
Explanation:
No letter occurs more than once in s, so the variance of every substring is 0.

Kadane's algorithm is a dynamic programming algorithm that finds the maximum subarray sum in an array of integers. It maintains two values: global_max, which represents the maximum sum encountered so far, and local_max, which represents the maximum sum ending at the current index. As the algorithm traverses the array from left to right, it updates these values. The algorithm is efficient because it only requires O(n) time and O(1) space to store two values and does not need any additional data structures.

As shown in the figure below, local_max represents the maximum value of the subarray ending at the current index. We update local_max at each index and update global_max by the maximum local_max. This ensures that we always have the maximum sum subarray at each position.
"""
class Solution:
    def largestVariance(self, s: str) -> int:
        countdict = Counter(s)

        global_ans = 0

        for a, b in itertools.product(set(s), set(s)):
            if a==b: continue

            count_a, count_b, reset_count_b = 0, 0, countdict[b]

            for ch in s:
                if ch == a: count_a += 1
                elif ch == b: 
                    count_b += 1
                    reset_count_b -= 1
                
                if count_b: global_ans = max(global_ans, count_a - count_b)
                if count_a - count_b < 0 and reset_count_b > 0:
                    count_a, count_b = 0, 0    


        return global_ans

