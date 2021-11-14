# time complexity : O(2n)
def count_negatives(given_array):
	count = 0
	row_i = 0 
	col_i = len(given_array[0])-1
	while col_i >= 0 and row_i < len(given_array):
		if given_array[row_i][col_i] < 0:
			count += (col_i + 1)
			row_i += 1
		else:
			col_i -= 1
	return count

print(
	count_negatives(
		[[-4, -3, -1, 1],
		[-2, -2, 1, 2],
		[-1, 1, 2, 3],
		[1, 2, 4, 5]]
		))

print(
	count_negatives(
		[[-2, 0],
		[-1, 0]]
		))