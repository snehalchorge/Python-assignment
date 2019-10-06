#Exercise 3

ac = [Aircraft() for x in range(5)]

ac[0].moveup()
ac[0].moveup()
ac[0].moveup()

print("The Final X,Y and Coordinates are:", ac[0].__dict__,)

ac[1].moveright()
ac[1].moveright()
ac[1].movedown()
ac[1].moveleft()

print("The Final X,Y and Coordinates are:", ac[1].__dict__,)



ac[2].movedown()
ac[2].moveleft()

print("The Final X,Y and Coordinates are:", ac[2].__dict__,)


ac[3].moveup()
ac[3].moveup()
ac[3].moveup()
ac[3].moveright()
ac[3].moveright()
print("The Final X,Y and Coordinates are:", ac[3].__dict__,)


ac[4].movedown()
ac[4].movedown()    
ac[4].moveup()
ac[4].moveleft()
ac[4].moveleft()
print("The Final X,Y and Coordinates are:", ac[4].__dict__,)
