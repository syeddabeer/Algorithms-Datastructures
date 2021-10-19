class Solution:
    def kClosest(self, points, k):
        if len(points)==k:
            return points
        
        d=[]
        
        for i in range(len(points)):
            d.append([((points[i][0])**2+(points[i][1])**2)**0.5, i])
            
        d.sort()
        
        output=[]
        for i in range(k):
            output.append(points[d[i][1]])
        return output

k=2
points=[[3,3],[5,-1],[-2,4]]
sol=Solution()
sol.kClosest(points, k)