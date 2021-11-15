def quicksort(arr):
	if len(arr) <=1:
		return arr 
	else:
		lesser, equal, greater = [], [], []
		pivot=arr[-1]
		for element in arr:
			if element<pivot:
				lesser.append(element)
			elif element>pivot:
				greater.append(element)
			else:
				equal.append(element)
		return quicksort(lesser)+equal+quicksort(greater)
	return arr 
list=[8,1,4,10,7,6,7,9,3,2,5]
print(quicksort(list))