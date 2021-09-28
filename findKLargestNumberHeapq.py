class Solution1:
    def largestKnumber(self, nums, k):
        nums.sort()
        return nums[-k]

import heapq
class Solution2: #heap method.
    def largestKnumber(self, nums, k):
        
        return heapq.nlargest(k, nums)[-1]
    
sol1=Solution1()
sol2=Solution2()
nums = [3,2,1,5,6,4]
k = 2
print(sol1.largestKnumber(nums, k))
print(sol2.largestKnumber(nums, k))