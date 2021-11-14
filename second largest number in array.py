def second_largest(mylist):
	largest = None 
	second_largest = None
	for num in mylist:
		if largest is None:
			largest = num
		elif num > largest:
			second_largest = largest
			largest = num
		elif second_largest is None:
			second_largest = num
		elif num > second_largest:
			second_largest = num 
	return second_largest

print(second_largest([1,3,4,5,0,2]))
print(second_largest([-2,-1]))
print(second_largest([2]))
print(second_largest([]))

