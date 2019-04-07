'''
A dictionary is a assoicative array, which has a key and a value 

d = {
    <key>: <value>,
    <key>: <value>,
    <key>: <value>
}

difference between list and dictionaries: Lists elements are accessed by numerical index based on order, and dictionary elements are accessed by key
'''
# different ways to create dictionaries 

d = {'foo': 100, 'bar': 200, 'baz': 300}

d = {}
d['foo'] = 100
d['bar'] = 200
d['baz'] = 300

d = dict([
    ('foo', 100),
    ('bar', 200),
    ('baz', 300)
])

d = dict(foo=100, bar=200, baz=300)
print(d)

# how to build a dictonary using key value dict! 
MLB_team = dict([
    ('colorado','rockies'),
    ('seattle','mariners'),
    ('new york','yankies')
])

MLB_team['LA'] = "dodgers"
print(MLB_team)

#What if you dont know the key value right away and want to build incrementally
person = {}
person['first_name'] = 'vijay'
person['last_name'] = 'patha'
person['role'] = 'product manager'

print(person)

del person['role']
print(person)

'patha' in person

# built-in dict functions 

# 1. clear()

d = {'a': 10, 'b': 20, 'c': 30}
print(d)

d.clear()
print(d) # gives an empty dictionary 

# 2..get(<key>[, <default>])
d = {'a': 10, 'b': 20, 'c': 30}
print(d.get('b'))

# 3: pop
d = {'a': 10, 'b': 20, 'c': 30}
print(d.pop('b'))

print(d)

# 4: items
d = {'a': 10, 'b': 20, 'c': 30}
print(d.items())

# Problem 1: Iterate 

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

for key, value in cast.items():
    print("Actor:{} Role:{}".format(key, value))

#Problem 3
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

result = 0 

for key, value in basket_items.items():
    if key in fruits:
        result += value # i need to add the values. WHere should I store them? 
print(result)

#Problem 4
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

fruits_count = 0
non_fruit_count = 0 

for key, value in basket_items.items():
    if key in fruits:
        fruits_count += value
    else:
        non_fruit_count += value
print("Total Fruits", fruits_count)
print("Total non-fruits", non_fruit_count)
