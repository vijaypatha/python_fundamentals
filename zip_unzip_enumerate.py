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


daily_chores = ["eat", "sleep", "repeat"]

for chore in enumerate(daily_chores):
    print (chore)
# chaning the counter to start at 300
for chore in enumerate(daily_chores,300):
    print (chore)


# STRING 
animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))

print("does your {} {}?".format(animal, action))

''' Map function 


'''

#Proble 1

# Return double of n 
def addition(n): 
    return(n + n)  
  
# We double all numbers using map() 
numbers = (1, 2, 3, 4)
result = map(addition, numbers) 
print(list(result))



numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)