# Zip

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ] 
  
# using zip() to map values 
mapped = zip(name, roll_no, marks)

mapped = list(mapped)

print(mapped)

# initializing list of players. 
players = [ "Sachin", "Sehwag", "Gambhir", "Dravid", "Raina" ] 
scores = [100, 15, 17, 28, 43 ] 

#print(list(zip(players, scores)))
lists = []
for lst in zip(players, scores):
    lists.append(lst)

for lst in lists:
    print(lst)

'''
Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends it to the list points. Each string should be formatted as label: x, y, z. For example, the string for the first coordinate should be F: 23, 677, 4. '''

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)


#Enummerate 
''' Enumerate
enumerate is a built in function that returns an iterator of tuples containing indices and values of a list. You'll often use this when you want the index along with each element of an iterable in a loop.'''

letters = ['a', 'b', 'c', 'd', 'e']
for index, letter in enumerate(letters):
    print(index, letter)

# STRING 
animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))

print("does your {} {}?".format(animal, action))