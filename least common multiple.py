# least common multiple
import sys
def lcm(a, b):
	return '%0.2d' %(a/gcd(a,b) * b)

def gcd(a, b):
	if b == 0:
		return a
	modulus = a%b
	return gcd(b, modulus)

if __name__ == '__main__':
	inputs = sys.stdin.read()
	a, b = map(int, inputs.split())
	# a, b = 444, 888
	print(lcm(a, b))