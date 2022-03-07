#253. Meeting Rooms II
class Solution:
	def minMeetingRooms(self, intervals):
		start=sorted([i[0] for i in intervals])
		end=sorted([i[1] for i in intervals])

		result = 0
		count = 0

		s_index=0 
		e_index=0 
		while s_index<len(intervals):
			if start[s_index] < end[e_index]:
				s_index+=1
				count+=1
			else:
				e_index+=1
				count-=1
			result = max(result, count)

		return result 

"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
"""