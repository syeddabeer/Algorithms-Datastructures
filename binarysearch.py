class Solution:
    def Search(self, nums, target): #nums is sorted list #complexity of the solution is log n
        
        if not nums:
            return -1
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = low + (high-low)//2
            
            if nums[mid] == target:
                return mid
                
            if target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
                
        return -1