#constraint: cannot use int() conversion
def larger_than(a, b):
	if len(a) > len(b):
		return True
	elif len(a) < len(b):
		return False
	for i in range(len(a)):
		if a[i] == b[i]:
			continue
		elif a[i] > b[i]:
			return True
		else: # a[i] < b[i]:
			return False
	return False

print(larger_than('112', '111'))
print(larger_than('525', '1111'))
print(larger_than('11', '0'))
print(larger_than('1', '1'))