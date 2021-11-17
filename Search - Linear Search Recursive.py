def recursiveLinearSearch(arr, low, high, x): # x is target
	if high < low:
		return -1
	if arr[low] == x:
		return low 
	if arr[high] == x:
		return high
	return recursiveLinearSearch(arr, low+1, high-1, x)

if __name__ == '__main__':
	arr = [2, 3, 4, 10, 40]
	target = 10
	print(recursiveLinearSearch(arr, 0, len(arr)-1, target))