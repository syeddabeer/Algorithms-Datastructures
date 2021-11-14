# revision file for strings

name = input("Enter the name:") # dynamic input

Apple = '210'
# if the following line gives error "Type Error"
x = Apple - 10
# TypeError - unsupported operand for str and int
x= int(Apple) - 10 # typecase into integer


# looking inside strings
fruit = 'banana'
letter = fruit[1]
print(letter) #a
x=3
w=fruit[x-1]
print(w) #n

# index out of error
zot ='abc'
print(zot[5]) #indexError: string index out of range

# len function
lengths=len(zot)
print(lengths)

# looping through strings
fruit = 'banana'
index = 0
while index < len(fruit):
	letter = fruit[index]
	print(index, letter)
	index = index + 1
# 0 b ; 1 a; 2 n; 3 a; 4 n; 5 a

# for loop
fruit = 'banana'
for letter in fruit:
	print(letter)
#b
#a
#n
#a
#n
#a

# for loop
for letter in 'banana':
	print(letter)
#b
#a
#n
#a
#n
#a

# count the number of a
fruit='banana'
count = 0
for i in fruit:
	if letter == 'a':
		count += 1
print(count)


# slicing
s[0:4]
# index 0, 1, 2, 3

s[:2]
# 0, 1

s[:]
# all elements

# string concatenation - string addition
a = 'Hello'
b = 'There'
c = a + ' ' + b
print(c)


#using 'in' as a logical operator
fruit = 'banana'
print('n' in fruit) #false
print('a' in fruit) #true