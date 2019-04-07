players = [ "Sachin", "Sehwag", "Gambhir", "Dravid", "Raina" ] 
scores = [100, 15, 17, 28, 43 ] 

#print(list(zip(players, scores)))
lists = []
for lst in zip(players, scores):
    lists.append(lst)

for lst in lists:
    print(lst)