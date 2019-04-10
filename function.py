'''
You can use lambda expressions to create anonymous functions. That is, functions that don’t have a name. They are helpful for creating quick functions that aren’t needed later in your code. This can be especially useful for higher order functions, or functions that take in other functions as arguments.
'''
#Example 
def multiply(x, y):
    print (x * y)
multiply(2,3)

multiply = lambda x, y: x * y
multiply(2,3)
print(multiply)

'''
Filter - 
takes a function and iterable as inputs and returns an iterator with the elements from the iterable for which the function returns True

'''

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)

# Using lamda function

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)
