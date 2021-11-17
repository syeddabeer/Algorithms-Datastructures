# maximise pairwise products
# def maximisePairwiseProducts(n, numbers):
# 	max_product=0
# 	for iter1 in range(n):
# 		for iter2 in range(iter1+1, n, 1):
# 			max_product=max(max_product, numbers[iter1]*numbers[iter2])
# 	return max_product

# if __name__ == '__main__':
# 	n=int(input())
# 	input_n = input()
# 	# input_text = '1 2 3 4 5 6 7 8 9'
# 	numbers = [int(x) for x in input_n.split()]
# 	print(maximisePairwiseProducts(n, dnumbers))

# Method - fast

def max_pairwise_product(numbers):
    n = len(numbers)
    input_numbers.sort()
    return input_numbers[-1]*input_numbers[-2]

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))