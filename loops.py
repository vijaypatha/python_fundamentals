# Problem 1: Covert a list to a usernames with lower caps and underscore between first and last name
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append (name.lower().replace(" ","_"))

print(usernames)

# Problem 2: Simplified version of problem 1
names: ["vijay patha", "heidi patha", "indigo patha"]

for name in names:
    print(name.lower().replace(" ","_"))

# problem 3: Create a function that takes a list and finds the integer which appears an odd number of times.
# Example: find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1

lst = [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]
def odd_repeats():
    for i in lst:
        lst.count(i % 2 !=0)
        print(i)



