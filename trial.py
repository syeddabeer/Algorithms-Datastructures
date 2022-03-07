class Solution:
    def minMeetingRooms(self, intervals):
        start = [i[0] for i in intervals]
        end = [i[1] for i in intervals]
        s=0
        e=0
        count = 0
        result = 0
        while s < len(intervals):
            if start[s] < end[e]:
                count+=1
                s+=1
            else:
                count-=1
                e+=1
            result = max(result, count)
        return result