'''
Practicing loops with varying degress of diffculties 
'''

# Problem 1: Covert a list to a usernames with lower caps and underscore between first and last name
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append (name.lower().replace(" ","_"))

print(usernames)


# Problem 2: Simplified version of problem 1
names = ["vijay patha", "heidi patha", "indigo patha"]

for name in names:
    print(name.lower().replace(" ","_"))

########################### Check Problem 3 ######################################
########################### Check Problem 3 ######################################

# Problem 3: Create a function that takes a list and finds the integer which appears an odd number of times.
# Example: find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1
def odd_repeats(lst = []):
    for i in lst:
        lst.count(i % 2 !=0) # any_list.count -> counts returns the number of occurrences 
        print(i)
items = [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]
odd_repeats(items)


#Problem  4: Find factors of a number 
def factorize(num):
	for i in range(1, num + 1):
		if num % i == 0:
			print(i)
factorize(5)

# v2

def factorin(num):
	lst = []
	for i in range(1,num+1):
		if num % i == 0:
			lst.append(i)
	print(lst)
factorin(40)



#Problem 5: Create a function that returns True if a number is prime and False if it's not
def prime_num(num):
	if num % 2 == 0:
			print(num, "is not a prime")
	else:
		print(num, "is a prime")
prime_num(12239)


# WHILE LOOP -> while loops are used when you don't know when the iteration should stop. For example if there are millions of data points and we need to find a data point that meets a certain condition. aka "indefinate iterations"


n = 5
while n > 0:
	n -= 1
	print(n)
'''
while n > 0 is header
n -= 1 is expression or body 

as long as or while n > 0, the loop will repeat the body n -= 1 and print one at a time 4,3,2,1
'''

n = 0 
while n > 0:
	n -= 1
	print(n)
# here it stops since the loop did not find any condition 

a = ['foo', 'bar', 'baz']
while a:
	print(a.pop())
print(a)

# Problem 6

# number to find the factorial of

Solution: While Loops Practice
Solution: Factorials with While Loops
Here is our solution for this one:


# number to find the factorial of
number = 6
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1

while  current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1


# print the factorial of number
print(product)


def factoriall(num):
	result = 1
	for i in range(1, num+1, 1):
		result *= i
		print(result)
factoriall(6)


num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

result = 0

for i in num_list:
    if i % 2 != 0:
        result += i
        print(result)

		

