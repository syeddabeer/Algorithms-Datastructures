# method 2
class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort()
        for i in range(0, len(intervals)-1, 1):
            if intervals[i][1] > intervals[i+1][0]:
                return False 
        return True

# brute force
class Solution:
    def canAttendMeetings(self, intervals):
        def overlap(interval1, interval2):
            return (interval1[0]>=interval2[0] and interval1[0]<interval2[1] or interval2[0]>=interval1[0] and interval2[0]<interval1[1])
        
        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):
                if overlap(intervals[i], intervals[j]):
                    return False
        return True
"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
"""