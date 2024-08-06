"""
15. 3Sum
"""
class Solution:
    def threeSum(self, nums):
        result=[] # This will store the unique triplets
        nums.sort() # Step 1: Sort the input array
        
        length=len(nums)
        
        for i in range(length-2): # Step 2: Iterate over the array
            if i>0 and nums[i]==nums[i-1]: # Skip duplicate elements for the first element of the triplet
                continue
            left = i+1 # Pointer for the second element
            right = length-1 # Pointer for the third element
            
            while left<right: # Step 3: Use two-pointer technique to find pairs
                total = nums[i]+nums[left]+nums[right]
                if total<0: # If the sum is less than the target, move the second pointer to the right
                    #-2,-1,0,1
                    left+=1
                elif total>0: # If the sum is greater than the target, move the third pointer to the left
                    right-=1
                else: # Step 4: Check if the triplet sum equals the target (0)
                    result.append([nums[i], nums[left], nums[right]])
                    left+=1 # Move the second pointer to the right
                    right-=1 # Move the third pointer to the left
                    
                    # Step 5: Skip duplicates for the second element
                    while left<right and nums[left]==nums[left+1]:
                        left+=1  
                    while left<right and nums[right]==nums[right-1]:
                        right-=1 
                    
        return result # Return the list of unique triplets

myobj=Solution()
nums = [-1,0,1,2,-1,-4]
print(myobj.threeSum(nums))

"""
time: O(n^2) - not confirmed
space: O(nlogn) - not confirmed

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""