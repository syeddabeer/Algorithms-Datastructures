class mergeIntervals:
    def merge(self, intervalsList):
        intervalsList.sort()
        merged=[]
        for iter in intervalsList:
            if not merged or merged[-1][1]<iter[0]:
                merged.append(iter)
            else:  #merged[-1][1] >= interval[0] #-1 indicates last interval in merged. #1 second number in the list
                merged[-1][1]=max(merged[-1][1], iter[1]) #the higher number in list -1,1 and interval[1] is initialized. #no need to add that interval to the merged list
        return merged
    
#validation
input1=[[1,3],[2,6],[8,10],[15,18]]
input2=[[1, 9], [2, 5], [19, 20], [10, 11], [12, 20], [0, 3], [0, 1], [0, 2]]
output1=mergeIntervals().merge(input1)
output2=mergeIntervals().merge(input2)
print("input1: ", input1)
print("output1: ", output1)
print("input2: ", input2)
print("output2: ", output2)

"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104