#1424. Diagonal Traverse II
class Solution(object):
    def findDiagonalOrder(self, A):
        res = []
        for i, r in enumerate(A):
            for j, a in enumerate(r):
                if len(res) <= i + j:
                    res.append([])
                    print('first loop res: {0}'.format(res))
                res[i + j].append(a)
                print('second loop res: {0}'.format(res))
        return [a for r in res for a in reversed(r)]

"""
alternative way:
		p=[]
        for i in res:
            p.extend(list(reversed(i)))
        return p
"""
"""
first loop res: [[]]
second loop res: [[1]]
first loop res: [[1], []]
second loop res: [[1], [2]]
first loop res: [[1], [2], []]
second loop res: [[1], [2], [3]]
second loop res: [[1], [2, 4], [3]]
second loop res: [[1], [2, 4], [3, 5]]
first loop res: [[1], [2, 4], [3, 5], []]
second loop res: [[1], [2, 4], [3, 5], [6]]
second loop res: [[1], [2, 4], [3, 5, 7], [6]]
second loop res: [[1], [2, 4], [3, 5, 7], [6, 8]]
first loop res: [[1], [2, 4], [3, 5, 7], [6, 8], []]
second loop res: [[1], [2, 4], [3, 5, 7], [6, 8], [9]]
"""

"""
Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.
Example 1:
Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
res = [1, 2, 3, , , , , , ]
Example 2:
Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
"""
