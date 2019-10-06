#Exercise 1 - Basic Aircraft problem

# PART 1
print("Exercise 1, part 1")
aircrafts = {'x':21, 'y':41}
#print(aircrafts.values())
for key,value in aircrafts.items():
    print(value)
    
#PART 2
print("\nExercise 1, part 2")
fleet=[]

aircrafts ={}
aircrafts['a'] =(63,0)
aircrafts['b'] = (65,0)
aircrafts ['c'] = (67,0)
aircrafts ['d'] = (69,0)
aircrafts['e'] = (71,0)

for key,value in aircrafts.items():
    print("X and Y coordinates are: ",value)
