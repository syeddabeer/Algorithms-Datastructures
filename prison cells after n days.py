class Solution:
	def prisonAfterNDays(self, cells, N):
		def nextDay(cells):
			mask = cells.copy()

			for i in range(1, len(cells)-1):
				if mask[i-1] ^ mask[i+1] == 0:
					cells[i] = 1 
				else:
					cells[i] = 0
				cells[0] = 0
				cells[-1] = 0 
			return cells
		print(cells)
		day1 = tuple(nextDay(cells))
		print(cells)
		N-=1
		count = 0

		while N>0:
			day = tuple(nextDay(cells))
			print(cells)
			N-=1
			count+=1

			if day==day1:
				N = N%count
		return cells




"""
There are 8 prison cells in a row and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.

You are given an integer array cells where cells[i] == 1 if the ith cell is occupied and cells[i] == 0 if the ith cell is vacant, and you are given an integer n.

Return the state of the prison after n days (i.e., n such changes described above).

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], n = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
"""