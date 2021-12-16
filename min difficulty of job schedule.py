from functools import lru_cache
class Solution:
	def minDifficulty(self, jobDifficulty, d):
		# @property is a decorator feature - a callable that returns callable. metaprogramming.
		n=len(jobDifficulty)
		if d > n: return -1
		
		#dp[day][j] = min(dp[day - 1][i -1] + max(difficulty[i:j])) for i in 0...j

		dp = [[0] + [float('inf')] * n for _ in range(d+1)] # array with 0 and infinities

		for i in range(1, d+1): # for all days
			for j in range(i, n+1): # for day num to all difficulties
				current = 0 
				for k in range(j, i-1, -1):
					current = max(current, jobDifficulty[k-1])
					dp[i][j] = min(dp[i][j], current+dp[i-1][k-1])
		return dp[-1][-1]


"""
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.
Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 
"""