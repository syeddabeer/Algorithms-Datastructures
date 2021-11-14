#LL 2-D array
def rooks_are_safe(chessboard):
	n = len(chessboard) #n cols = n rows
	for row_i in range(n):
		row_count = 0
		for col_i in range(n):
			row_count += chessboard[row_i][col_i]
		if row_count > 1:
			return False
	for col_i in range(n):
		col_count = 0
		for row_i in range(n):
			col_count += chessboard[row_i][col_i]
		if col_count > 1:
			return False	
	return True

print(
	rooks_are_safe(
	[[1, 0, 0, 0],
	[0, 1, 0, 0],
	[0, 0, 0, 1],
	[0, 0, 0, 0]]))

print(
	rooks_are_safe(
	[[1]]))

print(
	rooks_are_safe(
	[[1, 0],
	[1, 0]]))

print(
	rooks_are_safe(
	[[0, 0, 0],
	[1, 0, 1],
	[0, 0, 0]]))



