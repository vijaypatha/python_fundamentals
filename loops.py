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


