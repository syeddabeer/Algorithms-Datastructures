# greatest common divisor
import sys

def gcd_naive(a, b):
	temp_gcd = 1 
	for d in range(2, min(a, b) + 1):
		if a%d == 0 and b%d == 0:
			if d > temp_gcd:
				temp_gcd = d 
				# we will loop for all values. we want greatest of CD.
	return temp_gcd

if __name__ == '__main__':
	# input = sys.stdin.read()
	# a, b = map(int, input.split())
	a, b = 16, 144
	print(gcd_naive(a,b))