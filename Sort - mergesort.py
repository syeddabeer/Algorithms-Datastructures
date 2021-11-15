# divide and conquer method
# here there is no select pivot like the quick sort
# divide lists into half, then half, then half, until there is one element only
# then we start to merge the lists based on the sublists and for elements with less value.

def mergesort(arr):
	if len(arr)<=1:
		return arr
	mid = len(arr)//2
	
	firsthalf=arr[:mid]
	secondhalf=arr[mid:]
	
	half_a = mergesort(firsthalf)
	half_b = mergesort(secondhalf)
	
	return sortedMerge(half_a, half_b)
	
def sortedMerge(sublist1, sublist2):
	i = j = 0
	mergedlist = []
	
	while i<len(sublist1) and j<len(sublist2):
		if sublist1[i] < sublist2[j]:
			mergedlist.append(sublist1[i])
			i+=1
		else:
			mergedlist.append(sublist2[j])
			j+=1
	
	while i<len(sublist1):
		mergedlist.append(sublist1[i])
		i+=1
		
	while j<len(sublist2):
		mergedlist.append(sublist2[j])
		j+=1
		
	return mergedlist

list=[8,1,4,10,7,6,7,9,3,2,5]
print(mergesort(list))