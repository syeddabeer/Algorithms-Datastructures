"""
Breadth first search - prioritizes breadth over depth. traverses breadth before depth.
"""

from collections import deque 
class Solution:
	def orangesRotting(self, grid):
		
		rotten = deque()

		# build initial set of rotten oranges
		fresh_oranges = 0 
		rows, cols = len(grid), len(grid[0])

		for r in range(rows):
			for c in range(cols):
				if grid[r][c]==2:
					rotten.append((r,c))
				elif grid[r][c]==1:
					fresh_oranges+=1

		# timer
		minutes_passed = 0 

		# if there are rotten oranges, and fresh oranges, run loop
		while rotten and fresh_oranges>0: 
			# update minutes passed
			# update minutes safely by 1 everytime
			minutes_passed+=1

			# rotten array loop
			for i in range(len(rotten)):
				x, y = rotten.popleft()

				#visit all adjacent cells
				for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]: # L U R D
					# coordinates of adjacent cell
					xx, yy = x+dx, y+dy
					# ignore cell if out of geometry
					if xx<0 or xx==rows or yy<0 or yy==cols:
						continue
					#ignore cell if it is 0 or already rotten "2":
					if grid[xx][yy]==0 or grid[xx][yy]==2:
						continue
					#update the fresh oranges count
					fresh_oranges-=1

					#mark current fresh orange to rotten
					grid[xx][yy]=2

					#add current rotten to deque
					rotten.append((xx,yy))
		return minutes_passed if fresh_oranges==0 else -1








"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""