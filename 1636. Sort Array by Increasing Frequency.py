def frequencySort(self, nums):
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    # first by frequency, and then by number desc
    sorted_dict = sorted(dict.items(), key=lambda x: (x[1], -x[0]))
    print("{} is sorted_dict".format(sorted_dict))
    
    res = []
    
    for num, cnt in sorted_dict:
        temp = [num] * cnt
        res.extend(temp)
    return res
    

"""
1636. Sort Array by Increasing Frequency
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
"""
