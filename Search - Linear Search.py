def linearSearch(arr, x): # x is target
	n = len(arr)
	for i in range(len(arr)):
		if arr[i] == x:
			return 1 
	return -1

if __name__ == '__main__':
	arr = [2, 3, 4, 10, 40]
	target = 10
	print(linearSearch(arr, target))