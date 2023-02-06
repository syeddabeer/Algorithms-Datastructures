# 1010. Pairs of Songs With Total Durations Divisible by 60

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = collections.defaultdict(int) #default value when there is no key should be 0. that is why we took defaultdict(int)
        ret = 0
        for t in time:
            if t % 60 == 0: # check if a%60==0 && b%60==0
                ret += remainders[0]
            else: # check if a%60+b%60==60
                ret += remainders[60-t%60]
            remainders[t % 60] += 1 # remember to update the remainders
        return ret
"""
Complexity Analysis

Time complexity: \mathcal{O}(n)O(n), when nn is the length of the input array, because we would visit each element in time once.
Space complexity: \mathcal{O}(1)O(1), because the size of the array remainders is fixed with 6060.
"""
"""
ou are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 
 class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = collections.defaultdict(int)
        ret = 0
        print(f"remainders is {remainders}")
        print(f"ret is {ret}")
        for t in time:
            
            if t % 60 == 0: # check if a%60==0 && b%60==0
                ret += remainders[0]
            else: # check if a%60+b%60==60
                ret += remainders[60-t%60]
            remainders[t % 60] += 1 # remember to update the remainders
            print(f"t is {t}")
            print(f"ret is {ret}")
            print(f"remainders is {remainders}")
        return ret
        
remainders is defaultdict(<class 'int'>, {})
ret is 0
t is 30
ret is 0
remainders is defaultdict(<class 'int'>, {30: 1})
t is 20
ret is 0
remainders is defaultdict(<class 'int'>, {30: 1, 40: 0, 20: 1})
t is 150
ret is 1
remainders is defaultdict(<class 'int'>, {30: 2, 40: 0, 20: 1})
t is 100
ret is 2
remainders is defaultdict(<class 'int'>, {30: 2, 40: 1, 20: 1})
t is 40
ret is 3
remainders is defaultdict(<class 'int'>, {30: 2, 40: 2, 20: 1})   
 """