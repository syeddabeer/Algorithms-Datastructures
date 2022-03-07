#253. Meeting Rooms II
class Solution:
	def minMeetingRooms(self, intervals):
		start=sorted([i[0] for i in intervals])
		end=sorted([i[1] for i in intervals])

		result = 0 # in the whole, what is max room
		count = 0 # at a time, how many rooms are booked.

		s=0 # start index
		e=0 # end index
		while s<len(intervals):
			if start[s] < end[e]:
				s+=1
				count+=1
			else:
				e+=1
				count-=1
			result = max(result, count)

		return result 

"""
[[9,10],[4,9],[4,17]]
[[4,9],[4,17],[9,10]]

[[4,9],[4,17],[9,10]]

"""