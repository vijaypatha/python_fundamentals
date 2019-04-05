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
def odd_repeats(lst):
    for i in lst:
        lst.count(i % 2 !=0) # any_list.count -> counts returns the number of occurrences 
        print(i)
odd_repeats(lst = [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])


#Problem  4: Find factors of a number 
def factorize(num):
	for i in range(1, num + 1):
		if num % i == 0:
			print(i)
factorize(40)

########################### Check  Problem 5 ######################################
########################### Check Problem 5 ######################################

#Problem 5: Create a function that returns True if a number is prime and False if it's not
num = 4
if num > 1:
	for i in range(2, num):
		if (num % i == 0):
			print(num, "is not a prime")
	else:
		print(num, "is prime")
