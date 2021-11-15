# maximise pairwise products
def maximisePairwiseProducts(numbers):
	n=len(numbers)
	max_product=0
	for iter1 in range(n):
		for iter2 in range(iter1+1, n, 1):
			max_product=max(max_product, numbers[iter1]*numbers[iter2])
	return max_product

if __name__ == '__main__':
	# input_n = int(input())
	input_text = '1 2 3 4 5 6 7 8 9'
	numbers = [int(x) for x in input_text.split()]
	print(maximisePairwiseProducts(numbers))