class Solution:
	def maxArea(self, h, w, horizontalCuts, verticalCuts):
		#sort in asc order
		horizontalCuts.sort()
		verticalCuts.sort()

		#consider the edges first
		max_height = max(horizontalCuts[0], h - horizontalCuts[-1])

		#cuts in the middle
		for i in range(1, len(horizontalCuts)):
			max_height = max(max_height, horizontalCuts[i] - horizontalCuts[i-1])

		#consider the edges for the vertical edges
		max_width = max(verticalCuts[0], w - verticalCuts[-1])

		for i in range(1, len(verticalCuts)):
			max_width = max(max_width, verticalCuts[i] - verticalCuts[i-1])

		return (max_height*max_width)%(10**9 + 7)

"""
Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
"""		