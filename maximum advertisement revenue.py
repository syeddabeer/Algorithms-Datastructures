# maximum advertisement revenue
import sys

def max_dot_product(a, b):
	a.sort()
	b.sort()
	res = 0

	for i in range(len(a)):
		res += a[i]*b[i]

	return res

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n = data[0] # length 
	# n = 3
	a = data[1:(n+1)] # first array
	# a = [1, 3, -5]
	b = data[(n+1):] # second array
	# b = [-2, 4, 1]
	print(max_dot_product(a, b))




