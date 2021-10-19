# Function for nth Fibonacci number
 
def fib(n):
    if n < 0:
        print("invalid number")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
#validation
num=int(input('input the number of fibonacci numbers you wish to get:'))
for i in range(0, num, 1):
    print(fib(i))