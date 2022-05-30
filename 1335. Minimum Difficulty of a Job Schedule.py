from functools import lru_cache
class Solution:
	def minDifficulty(self, jobDifficulty, d):
		# @property is a decorator feature - a callable that returns callable. metaprogramming.
		n=len(jobDifficulty)
		if d > n: return -1
		
		#dp[day][j] = min(dp[day - 1][i -1] + max(difficulty[i:j])) for i in 0...j

		dp = [[0] + [float('inf')] * n for _ in range(d+1)] # array of 'd+1' sub-arrays. each sub-array with 0 and 'len(diff)' infinities

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

"""
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n=len(jobDifficulty)
        
        if d>n: return -1
        
        dp=[[0]+[float('inf')]*n for _ in range(d+1)]
        print(f"outside loop: dp: {dp}")
        
        for i in range(d+1):
            print(f"inside i loop: i: {i}")
            for j in range(i, n+1):
                print(f"inside j loop: j: {j}")
                current=0
                for k in range(j, i-1, -1):
                    current=max(current, jobDifficulty[k-1])
                    print(f"inside k loop: k: {k}")
                    print(f"inside k loop: current: {current}")
                    dp[i][j]=min(dp[i][j], current+dp[i-1][k-1])
                    print(f"inside k loop: dp: {dp}")
        return dp[-1][-1]
 
outside loop: dp: [[0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside i loop: i: 0
inside j loop: j: 0
inside k loop: k: 0
inside k loop: current: 1
inside k loop: dp[0][0]: 0
inside k loop: dp: [[0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside j loop: j: 1
inside k loop: k: 1
inside k loop: current: 6
inside k loop: dp[0][1]: 6
inside k loop: dp: [[0, 6, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 0
inside k loop: current: 6
inside k loop: dp[0][1]: 6
inside k loop: dp: [[0, 6, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside j loop: j: 2
inside k loop: k: 2
inside k loop: current: 5
inside k loop: dp[0][2]: inf
inside k loop: dp: [[0, 6, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 1
inside k loop: current: 6
inside k loop: dp[0][2]: 6
inside k loop: dp: [[0, 6, 6, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 0
inside k loop: current: 6
inside k loop: dp[0][2]: 6
inside k loop: dp: [[0, 6, 6, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside j loop: j: 3
inside k loop: k: 3
inside k loop: current: 4
inside k loop: dp[0][3]: inf
inside k loop: dp: [[0, 6, 6, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 2
inside k loop: current: 5
inside k loop: dp[0][3]: inf
inside k loop: dp: [[0, 6, 6, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 1
inside k loop: current: 6
inside k loop: dp[0][3]: 6
inside k loop: dp: [[0, 6, 6, 6, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 0
inside k loop: current: 6
inside k loop: dp[0][3]: 6
inside k loop: dp: [[0, 6, 6, 6, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside j loop: j: 4
inside k loop: k: 4
inside k loop: current: 3
inside k loop: dp[0][4]: inf
inside k loop: dp: [[0, 6, 6, 6, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 3
inside k loop: current: 4
inside k loop: dp[0][4]: inf
inside k loop: dp: [[0, 6, 6, 6, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 2
inside k loop: current: 5
inside k loop: dp[0][4]: inf
inside k loop: dp: [[0, 6, 6, 6, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 1
inside k loop: current: 6
inside k loop: dp[0][4]: 6
inside k loop: dp: [[0, 6, 6, 6, 6, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 0
inside k loop: current: 6
inside k loop: dp[0][4]: 6
inside k loop: dp: [[0, 6, 6, 6, 6, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside j loop: j: 5
inside k loop: k: 5
inside k loop: current: 2
inside k loop: dp[0][5]: inf
inside k loop: dp: [[0, 6, 6, 6, 6, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 4
inside k loop: current: 3
inside k loop: dp[0][5]: inf
inside k loop: dp: [[0, 6, 6, 6, 6, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 3
inside k loop: current: 4
inside k loop: dp[0][5]: inf
inside k loop: dp: [[0, 6, 6, 6, 6, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 2
inside k loop: current: 5
inside k loop: dp[0][5]: inf
inside k loop: dp: [[0, 6, 6, 6, 6, inf, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 1
inside k loop: current: 6
inside k loop: dp[0][5]: 6
inside k loop: dp: [[0, 6, 6, 6, 6, 6, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 0
inside k loop: current: 6
inside k loop: dp[0][5]: 6
inside k loop: dp: [[0, 6, 6, 6, 6, 6, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside j loop: j: 6
inside k loop: k: 6
inside k loop: current: 1
inside k loop: dp[0][6]: inf
inside k loop: dp: [[0, 6, 6, 6, 6, 6, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 5
inside k loop: current: 2
inside k loop: dp[0][6]: inf
inside k loop: dp: [[0, 6, 6, 6, 6, 6, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 4
inside k loop: current: 3
inside k loop: dp[0][6]: inf
inside k loop: dp: [[0, 6, 6, 6, 6, 6, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 3
inside k loop: current: 4
inside k loop: dp[0][6]: inf
inside k loop: dp: [[0, 6, 6, 6, 6, 6, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 2
inside k loop: current: 5
inside k loop: dp[0][6]: inf
inside k loop: dp: [[0, 6, 6, 6, 6, 6, inf], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 1
inside k loop: current: 6
inside k loop: dp[0][6]: 6
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 0
inside k loop: current: 6
inside k loop: dp[0][6]: 6
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, inf, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside i loop: i: 1
inside j loop: j: 1
inside k loop: k: 1
inside k loop: current: 6
inside k loop: dp[1][1]: 6
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside j loop: j: 2
inside k loop: k: 2
inside k loop: current: 5
inside k loop: dp[1][2]: 11
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 11, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 1
inside k loop: current: 6
inside k loop: dp[1][2]: 6
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside j loop: j: 3
inside k loop: k: 3
inside k loop: current: 4
inside k loop: dp[1][3]: 10
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 10, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 2
inside k loop: current: 5
inside k loop: dp[1][3]: 10
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 10, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 1
inside k loop: current: 6
inside k loop: dp[1][3]: 6
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, inf, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside j loop: j: 4
inside k loop: k: 4
inside k loop: current: 3
inside k loop: dp[1][4]: 9
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 9, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 3
inside k loop: current: 4
inside k loop: dp[1][4]: 9
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 9, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 2
inside k loop: current: 5
inside k loop: dp[1][4]: 9
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 9, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 1
inside k loop: current: 6
inside k loop: dp[1][4]: 6
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, inf, inf], [0, inf, inf, inf, inf, inf, inf]]
inside j loop: j: 5
inside k loop: k: 5
inside k loop: current: 2
inside k loop: dp[1][5]: 8
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 8, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 4
inside k loop: current: 3
inside k loop: dp[1][5]: 8
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 8, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 3
inside k loop: current: 4
inside k loop: dp[1][5]: 8
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 8, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 2
inside k loop: current: 5
inside k loop: dp[1][5]: 8
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 8, inf], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 1
inside k loop: current: 6
inside k loop: dp[1][5]: 6
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, inf], [0, inf, inf, inf, inf, inf, inf]]
inside j loop: j: 6
inside k loop: k: 6
inside k loop: current: 1
inside k loop: dp[1][6]: 7
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 7], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 5
inside k loop: current: 2
inside k loop: dp[1][6]: 7
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 7], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 4
inside k loop: current: 3
inside k loop: dp[1][6]: 7
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 7], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 3
inside k loop: current: 4
inside k loop: dp[1][6]: 7
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 7], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 2
inside k loop: current: 5
inside k loop: dp[1][6]: 7
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 7], [0, inf, inf, inf, inf, inf, inf]]
inside k loop: k: 1
inside k loop: current: 6
inside k loop: dp[1][6]: 6
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 6], [0, inf, inf, inf, inf, inf, inf]]
inside i loop: i: 2
inside j loop: j: 2
inside k loop: k: 2
inside k loop: current: 5
inside k loop: dp[2][2]: 11
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 6], [0, inf, 11, inf, inf, inf, inf]]
inside j loop: j: 3
inside k loop: k: 3
inside k loop: current: 4
inside k loop: dp[2][3]: 10
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 6], [0, inf, 11, 10, inf, inf, inf]]
inside k loop: k: 2
inside k loop: current: 5
inside k loop: dp[2][3]: 10
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 6], [0, inf, 11, 10, inf, inf, inf]]
inside j loop: j: 4
inside k loop: k: 4
inside k loop: current: 3
inside k loop: dp[2][4]: 9
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 6], [0, inf, 11, 10, 9, inf, inf]]
inside k loop: k: 3
inside k loop: current: 4
inside k loop: dp[2][4]: 9
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 6], [0, inf, 11, 10, 9, inf, inf]]
inside k loop: k: 2
inside k loop: current: 5
inside k loop: dp[2][4]: 9
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 6], [0, inf, 11, 10, 9, inf, inf]]
inside j loop: j: 5
inside k loop: k: 5
inside k loop: current: 2
inside k loop: dp[2][5]: 8
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 6], [0, inf, 11, 10, 9, 8, inf]]
inside k loop: k: 4
inside k loop: current: 3
inside k loop: dp[2][5]: 8
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 6], [0, inf, 11, 10, 9, 8, inf]]
inside k loop: k: 3
inside k loop: current: 4
inside k loop: dp[2][5]: 8
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 6], [0, inf, 11, 10, 9, 8, inf]]
inside k loop: k: 2
inside k loop: current: 5
inside k loop: dp[2][5]: 8
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 6], [0, inf, 11, 10, 9, 8, inf]]
inside j loop: j: 6
inside k loop: k: 6
inside k loop: current: 1
inside k loop: dp[2][6]: 7
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 6], [0, inf, 11, 10, 9, 8, 7]]
inside k loop: k: 5
inside k loop: current: 2
inside k loop: dp[2][6]: 7
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 6], [0, inf, 11, 10, 9, 8, 7]]
inside k loop: k: 4
inside k loop: current: 3
inside k loop: dp[2][6]: 7
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 6], [0, inf, 11, 10, 9, 8, 7]]
inside k loop: k: 3
inside k loop: current: 4
inside k loop: dp[2][6]: 7
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 6], [0, inf, 11, 10, 9, 8, 7]]
inside k loop: k: 2
inside k loop: current: 5
inside k loop: dp[2][6]: 7
inside k loop: dp: [[0, 6, 6, 6, 6, 6, 6], [0, 6, 6, 6, 6, 6, 6], [0, inf, 11, 10, 9, 8, 7]]
    
"""