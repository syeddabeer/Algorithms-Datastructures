def insertionSort(arr):
	for main_index in range(1, len(arr)):
		referenceValue=arr[main_index]

		working_index=main_index-1
		while working_index>=0:
			if arr[working_index+1]<arr[working_index]:
				arr[working_index+1], arr[working_index] = arr[working_index], arr[working_index+1]
			working_index-=1

# Driver code to test above
arr = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
insertionSort(arr)
print ("Sorted array is:")
print(arr)
