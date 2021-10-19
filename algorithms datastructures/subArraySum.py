#Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

class subArraySumClass:
    def subArraySum(self, nums, k): #nums is a list, k is the number
    # nums = [3,4,7,2,-3,1,4,2]
    # k = 7
        leng=len(nums)
        cumv, count = 0, 0
        hashmap = {0: 1}
        for i in range(leng):
            cumv += nums[i]
            if cumv-k in hashmap:
                count += hashmap[cumv-k]
            if cumv not in hashmap:
                hashmap[cumv]=0
            hashmap[cumv] += 1
        return count
        
RunObject = subArraySumClass()
nums = [3,4,7,2,-3,1,4,2]
k = 7
RunObject.subArraySum(nums, k)
