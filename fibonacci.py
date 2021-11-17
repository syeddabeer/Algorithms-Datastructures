def fibonacci(n, result=[0,1]):
	if n==0:
		return result[0:1]
	elif n==1:
		return result[:]
	while n>=len(result):
		result.append(result[-1] + result[-2])
	return result

if __name__ == '__main__':
    # input_n = int(input())
    input_n = 1
    print(fibonacci(input_n))
